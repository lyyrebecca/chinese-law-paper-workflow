#!/usr/bin/env python3
"""Local regression tests. Synthetic fixtures are not real sources or verification evidence."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile
from xml.etree import ElementTree as ET
import project

ROOT=Path(__file__).resolve().parents[1]

class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.p=Path(self.tmp.name)
        self.paper=self.p/'paper.md'; self.paper.write_text('# 合成测试稿\n\n这是自建测试材料的说明。[^N001]\n\n[^N001]: 合成材料，第1段。\n',encoding='utf-8')
        self.source=self.p/'evidence.txt'; self.source.write_text('这是自建测试材料。',encoding='utf-8')
        self.registry=self.p/'sources.json'
        self.reg={'schema_version':1,'sources':[{'id':'S001','kind':'online','title':'合成测试材料','creator':'本地测试','location':str(self.source),'file':'evidence.txt','sha256':hashlib.sha256(self.source.read_bytes()).hexdigest(),'access':'EXCERPT','status':'VERIFIED','verified_at':'2026-10-22'}],'notes':[{'key':'N001','supports':[{'source_id':'S001','locator':'第1段','claim':'自建材料内容','support_scope':'仅此段','support_checked':True}]}]}
        self.save()
    def tearDown(self): self.tmp.cleanup()
    def save(self): self.registry.write_text(json.dumps(self.reg,ensure_ascii=False),encoding='utf-8')
    def codes(self,final=True,files=False): return {x['code'] for x in project.audit(self.paper,self.registry,final,files)['findings']}
    def run_tool(self,*args): return subprocess.run([sys.executable,str(ROOT/'scripts/toolbox.py'),*map(str,args)],capture_output=True,text=True)
    def test_01_init_course(self):
        project.init_project(self.p/'new','课程题目','course','2026-10-22')
        self.assertTrue((self.p/'new/02_研究/sources.json').exists())
    def test_02_init_no_overwrite(self):
        with self.assertRaises(ValueError): project.init_project(self.p,'x','course',None)
        self.assertTrue(self.paper.exists())
    def test_03_init_longform(self):
        project.init_project(self.p/'new','长篇','longform',None)
        self.assertTrue((self.p/'new/00_管理/长篇批次.md').exists())
    def test_04_valid_registry_structural_only(self):
        result=project.audit(self.paper,self.registry,True,True)
        self.assertFalse(result['findings']); self.assertIn('semantic support',result['NOT_ASSESSED'])
    def test_05_missing_note(self):
        self.paper.write_text('引用[^N002]',encoding='utf-8'); self.assertIn('MISSING_NOTE',self.codes())
    def test_06_duplicate_note(self):
        self.paper.write_text(self.paper.read_text()+'\n[^N001]: 重复\n',encoding='utf-8'); self.assertIn('DUPLICATE_NOTE',self.codes())
    def test_07_orphan(self):
        self.paper.write_text('[^X]: 孤立定义',encoding='utf-8'); self.assertIn('ORPHAN_NOTE',self.codes())
    def test_08_placeholder_retained(self):
        self.paper.write_text(self.paper.read_text()+'\n[待补页码]',encoding='utf-8'); self.assertIn('PLACEHOLDER',self.codes())
    def test_09_core_not_verified(self):
        self.reg['sources'][0]['relevance']='CORE'; self.reg['sources'][0]['status']='LEAD_ONLY'; self.save(); self.assertIn('SOURCE_NOT_VERIFIED',self.codes())
    def test_10_unknown_source(self):
        self.reg['notes'][0]['supports'][0]['source_id']='S999'; self.save(); self.assertIn('UNKNOWN_SOURCE',self.codes())
    def test_11_missing_locator(self):
        del self.reg['notes'][0]['supports'][0]['locator']; self.save(); self.assertIn('INCOMPLETE_SUPPORT',self.codes())
    def test_12_no_semantic_attestation(self):
        self.reg['notes'][0]['supports'][0]['support_checked']=False; self.save(); self.assertIn('SUPPORT_NOT_ATTESTED',self.codes())
    def test_13_file_drift(self):
        self.source.write_text('已更改',encoding='utf-8'); self.assertIn('SOURCE_DRIFT',self.codes(files=True))
    def test_14_law_version(self):
        self.reg['sources'][0]['kind']='law'; self.save(); self.assertIn('LEGAL_VERSION_GAP',self.codes())
    def test_15_author_note(self):
        self.reg['notes'][0]={'key':'N001','author_note':True,'reasoning':'作者对本文前提的补充推理'}; self.save(); self.assertFalse(self.codes())
    def test_16_bad_schema(self):
        self.registry.write_text('[]',encoding='utf-8')
        with self.assertRaises(ValueError): project.audit(self.paper,self.registry,True)
    def test_17_code_not_citation(self):
        self.paper.write_text(self.paper.read_text()+'\n```md\n[^N999]\n```\n',encoding='utf-8'); self.assertNotIn('MISSING_NOTE',self.codes())
    def test_18_distinct_notes_same_source(self):
        self.paper.write_text(self.paper.read_text()+'\n第二处[^N002]\n\n[^N002]: 同源不同位置。\n',encoding='utf-8')
        self.reg['notes'].append({'key':'N002','supports':[dict(self.reg['notes'][0]['supports'][0],locator='第2句',claim='另一用途')]}); self.save(); self.assertFalse(self.codes())
    def test_19_parse_cnki_dedupe(self):
        source=self.p/'ref.txt'; source.write_text('%0 Journal Article\n%A 测试作者\n%T 合成题录不可作为文献\n%J 合成测试刊\n%D 2020\n%N 1\n%P 1-3\n\n%0 Journal Article\n%A 测试作者\n%T 合成题录不可作为文献\n%J 合成测试刊\n%D 2020\n%N 1\n%P 1-3\n',encoding='utf-8')
        output=self.p/'refs.tsv'; r=self.run_tool('parse-cnki',source,'--out',output)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr); self.assertEqual(len(output.read_text().splitlines()),2)
    def test_20_normalize_no_overwrite(self):
        output=self.p/'new.md'; before=self.paper.read_bytes(); r=self.run_tool('normalize',self.paper,'--out',output)
        self.assertEqual(r.returncode,0,r.stderr); self.assertEqual(self.paper.read_bytes(),before)
        self.assertEqual(self.run_tool('normalize',self.paper,'--out',output).returncode,2)
    def test_21_review_retains_gaps(self):
        self.paper.write_text(self.paper.read_text()+'\n[待核：来源]\n',encoding='utf-8')
        output=self.p/'review'; r=self.run_tool('review-packet',self.paper,'--out',output)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        self.assertTrue(any('[待核：来源]' in f.read_text() for f in output.glob('*.md')))
    def test_22_numeric_renumber_source_unchanged(self):
        self.paper.write_text('文字[2]。\n\n## 参考文献\n\n[1] 未用合成项[J]. 2020:1.\n[2] 已用合成项[J]. 2020:2.\n',encoding='utf-8'); before=self.paper.read_bytes()
        r=self.run_tool('renumber',self.paper,'--out',self.p/'new.md')
        self.assertEqual(r.returncode,0,r.stdout+r.stderr); self.assertEqual(self.paper.read_bytes(),before)
    def test_23_docx_real_notes_in_body_and_table(self):
        if not importlib.util.find_spec('docx'): self.skipTest('python-docx unavailable')
        self.paper.write_text('# 合成测试稿\n\n## 摘要\n\n测试稳定脚注键的真实转换。\n\n关键词：测试；脚注\n\n## 论证\n\n正文内容。[^N001]\n\n| 项目 | 说明 |\n|---|---|\n| A | 表内脚注[^N002] |\n\n[^N001]: 合成材料甲，第1段。\n[^N002]: 合成材料乙，第2段。\n',encoding='utf-8')
        out=self.p/'paper.docx'; r=self.run_tool('docx',self.paper,'--out',out)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        with zipfile.ZipFile(out) as z:
            ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            doc=ET.fromstring(z.read('word/document.xml')); foot=ET.fromstring(z.read('word/footnotes.xml'))
            self.assertEqual(len(doc.findall('.//w:footnoteReference',ns)),2)
            self.assertEqual(len(foot.findall('w:footnote',ns)),4)
            texts=''.join(doc.itertext()); self.assertIn('关键词：测试；脚注',texts); self.assertNotIn('作者信息',texts)
    def test_24_docx_reject_disappearing_notes(self):
        if not importlib.util.find_spec('docx'): self.skipTest('python-docx unavailable')
        self.assertEqual(self.run_tool('docx',self.paper,'--out',self.p/'p.docx','--profile','journal').returncode,2)
    def test_25_source_snapshot_checksums(self):
        m=json.loads((ROOT/'references/source-manifest.json').read_text())
        self.assertEqual(len({x['source_id'] for x in m['files']}),10)
        for f in m['files']: self.assertEqual(hashlib.sha256((ROOT/f['bundled_path']).read_bytes()).hexdigest(),f['sha256'])
    def test_26_single_discoverable_skill(self):
        self.assertEqual(list(ROOT.rglob('SKILL.md')),[ROOT/'SKILL.md'])
    def test_27_structural_diff_contract(self):
        r=subprocess.run([sys.executable,str(ROOT/'references/source-library/S06/scripts/validate_structural_edit.py'),str(ROOT/'references/source-library/S06/tests/fixtures/framework_edit_contract.json')],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
    def test_28_case_identity(self):
        self.reg['sources'][0]['kind']='case'; self.save(); self.assertIn('CASE_IDENTITY_GAP',self.codes())
    def test_29_structure_rejects_token_only_claim(self):
        outline=[{'id':'A','title':'原题','children':[{'id':'a','title':'原项'}]}]
        case={'baseline_outline':outline,'revision_outline':[{'id':'A','title':'换词','children':[{'id':'a','title':'换词项'}]}],'claim':'structural_change'}
        p=self.p/'case.json'; p.write_text(json.dumps(case),encoding='utf-8')
        r=self.run_tool('structure-check',p); self.assertEqual(r.returncode,1,r.stdout+r.stderr)
    def test_30_review_keeps_hidden_gaps_not_personal_rules(self):
        self.paper.write_text('> 作者：合成身份\n\n正常学者名字不应全局删除。\n<!-- 待核：缺少依据 -->',encoding='utf-8')
        out=self.p/'review'; r=self.run_tool('review-packet',self.paper,'--out',out,'--anonymize')
        self.assertEqual(r.returncode,0,r.stdout+r.stderr)
        draft=(out/'审稿稿_M1.md').read_text(); task=(out/'审稿任务说明_M1.md').read_text()
        self.assertIn('缺少依据',draft); self.assertNotIn('合成身份',draft); self.assertIn('正常学者名字',draft)
        self.assertIn('不会自动启动',task); self.assertNotIn('必须新建',task)

if __name__=='__main__': unittest.main(verbosity=2)
