#!/usr/bin/env python3
"""Initialize a non-overwriting paper project and audit structural evidence records.

No network, no automatic verification-status upgrades, no manuscript mutation.
Exit: 0 checked invariants pass; 1 findings; 2 invalid input. Not a legal/semantic verifier.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
DEF = re.compile(r'^ {0,3}\[\^([^\]\s]+)\]:\s*(.*)$')
REF = re.compile(r'\[\^([^\]\s]+)\](?!:)')
GAP = re.compile(r'\[(?:待[^\]\n]+|缺[^\]\n]*|需核[^\]\n]*|来源不明[^\]\n]*|VERIFY[^\]\n]*)\]|\b(?:TODO|TBD|FIXME)\b', re.I)
STATUSES = {'VERIFIED', 'PARTIAL', 'LEAD_ONLY', 'UNUSABLE'}
ACCESS = {'METADATA', 'ABSTRACT', 'EXCERPT', 'FULLTEXT'}

def load_registry(path):
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('sources.json requires schema_version=1')
    for key in ('sources', 'notes'):
        if not isinstance(data.get(key), list) or any(not isinstance(x, dict) for x in data[key]):
            raise ValueError(f'{key} must be a list of objects')
    for src in data['sources']:
        if not isinstance(src.get('id'), str) or not src['id'].strip():
            raise ValueError('each source requires a string id')
        if src.get('status') not in STATUSES or src.get('access') not in ACCESS:
            raise ValueError(f"invalid status/access for {src['id']}")
    for note in data['notes']:
        if not isinstance(note.get('key'), str) or not note['key'].strip():
            raise ValueError('each note requires a string key')
        supports = note.get('supports', [])
        if not isinstance(supports, list) or any(not isinstance(x, dict) for x in supports):
            raise ValueError('note.supports must be a list of objects')
    return data

def parse_markdown(text):
    """Simple Markdown footnotes, preserving line positions; skip fenced code examples."""
    body, definitions = [], []
    in_fence = None
    pending = None
    for number, line in enumerate(text.splitlines(), 1):
        fence = re.match(r'^\s*(`{3,}|~{3,})', line)
        if fence:
            char = fence.group(1)[0]
            if in_fence is None: in_fence = (char, len(fence.group(1)))
            elif char == in_fence[0] and len(fence.group(1)) >= in_fence[1]: in_fence = None
            pending = None
            continue
        if in_fence: continue
        match = DEF.match(line)
        if match:
            pending = {'key': match.group(1), 'text': match.group(2), 'line': number}
            definitions.append(pending)
        elif pending is not None and (line.startswith('    ') or line.startswith('\t')):
            pending['text'] += '\n' + line.lstrip()
        else:
            pending = None
            body.append((number, line))
    return body, definitions

def audit(path, registry=None, final=False, check_files=False):
    text = path.read_text(encoding='utf-8-sig')
    findings = []
    def add(code, message, line=None, severity='error'):
        item = {'code': code, 'severity': severity, 'message': message}
        if line is not None: item['line'] = line
        findings.append(item)
    body, definitions = parse_markdown(text)
    refs = [(n, m.group(1)) for n, line in body for m in REF.finditer(line)]
    keys = [x['key'] for x in definitions]
    for key, count in Counter(keys).items():
        if count > 1: add('DUPLICATE_NOTE', f'{key}: {count} definitions')
    for n, key in refs:
        if key not in keys: add('MISSING_NOTE', f'{key}: reference without definition', n)
    used = {k for _, k in refs}
    for d in definitions:
        if d['key'] not in used: add('ORPHAN_NOTE', f"{d['key']}: unused definition", d['line'])
        if not d['text'].strip(): add('EMPTY_NOTE', f"{d['key']}: empty definition", d['line'])
    for key, count in Counter(k for _, k in refs).items():
        if count > 1:
            add('REPEATED_NOTE_KEY', f'{key}: repeated {count} times; confirm cross-reference or use occurrence keys', severity='warning')
    # Gaps inside prose, definitions and even comments are retained; code examples are not ignored here.
    for n, line in enumerate(text.splitlines(), 1):
        for m in GAP.finditer(line):
            add('PLACEHOLDER', m.group(0), n, 'error' if final else 'warning')
    if any(re.search(r'(?<!\^)\[\d+(?:[-,，]\d+)*\]', line) for _, line in body):
        add('NUMERIC_CITATIONS_NOT_ASSESSED', 'Use toolbox validate-refs for numeric bibliography citations.', severity='warning')
    if registry is None:
        add('REGISTRY_NOT_ASSESSED', 'No source register; existence, support and legal validity NOT assessed.', severity='error' if final and used else 'warning')
    else:
        data = load_registry(registry)
        sources = {x['id']: x for x in data['sources']}
        notes = {x['key']: x for x in data['notes']}
        for label, entries, key in [('SOURCE', data['sources'], 'id'), ('NOTE_MAP', data['notes'], 'key')]:
            for ident, count in Counter(x[key] for x in entries).items():
                if count > 1: add('DUPLICATE_' + label, f'{ident}: duplicate registry entry')
        for key in sorted(used):
            note = notes.get(key)
            if note is None:
                add('UNMAPPED_NOTE', f'{key}: no note→source mapping', severity='error' if final else 'warning')
                continue
            if note.get('author_note') is True:
                if not note.get('reasoning'): add('AUTHOR_NOTE_REASONING', f'{key}: describe authored reasoning')
                if note.get('supports'): add('MIXED_AUTHOR_NOTE', f'{key}: author_note must not hide external supports')
                continue
            if not note.get('supports'): add('NO_SUPPORTS', f'{key}: no registered source support')
            for support in note.get('supports', []):
                sid = support.get('source_id')
                if not isinstance(sid, str):
                    raise ValueError(f'{key}: source_id must be a string')
                src = sources.get(sid)
                if src is None:
                    add('UNKNOWN_SOURCE', f'{key}: unknown source {sid}')
                    continue
                for field in ('locator', 'claim', 'support_scope'):
                    if not isinstance(support.get(field), str) or not support[field].strip():
                        add('INCOMPLETE_SUPPORT', f'{key}/{sid}: missing {field}', severity='error' if final else 'warning')
                if src['status'] != 'VERIFIED':
                    add('SOURCE_NOT_VERIFIED', f'{key}/{sid}: {src["status"]}', severity='error' if final else 'warning')
                if support.get('support_checked') is not True:
                    add('SUPPORT_NOT_ATTESTED', f'{key}/{sid}: no manual support check recorded', severity='error' if final else 'warning')
                for field in ('kind', 'title', 'creator', 'location', 'verified_at'):
                    if not isinstance(src.get(field), str) or not src[field].strip():
                        add('INCOMPLETE_SOURCE', f'{sid}: missing {field}', severity='error' if final else 'warning')
                if src.get('verified_at'):
                    try: date.fromisoformat(src['verified_at'])
                    except (ValueError, TypeError): add('INVALID_DATE', f'{sid}: verified_at must be YYYY-MM-DD')
                if src.get('kind') in ('law', 'judicial_interpretation', 'regulation', 'normative_document'):
                    for field in ('version', 'valid_at', 'legal_identity'):
                        if not src.get(field): add('LEGAL_VERSION_GAP', f'{sid}: missing {field}')
                if src.get('kind') == 'case':
                    for field in ('case_number', 'court', 'decision_date', 'document_type'):
                        if not src.get(field): add('CASE_IDENTITY_GAP', f'{sid}: missing {field}')
                if check_files and src.get('file'):
                    if not isinstance(src['file'], str): raise ValueError(f'{sid}: file must be a string')
                    f = Path(src['file'])
                    if not f.is_absolute(): f = registry.parent/f
                    if not f.is_file(): add('SOURCE_FILE_MISSING', f'{sid}: {f}')
                    elif not src.get('sha256'):
                        add('SOURCE_HASH_MISSING', f'{sid}: no stored SHA-256', severity='warning')
                    elif hashlib.sha256(f.read_bytes()).hexdigest() != src['sha256']:
                        add('SOURCE_DRIFT', f'{sid}: file hash changed; recheck affected claims')
        for key in notes.keys()-used:
            add('UNUSED_NOTE_MAP', f'{key}: mapping not used in this manuscript', severity='warning')
    return {
        'file': str(path.resolve()), 'scope': 'mechanical structure and registry completeness only',
        'NOT_ASSESSED': ['source authenticity', 'quotation accuracy', 'semantic support', 'current legal validity', 'argument quality', 'document layout'],
        'final_requested': final,
        'stats': {'chinese_characters': len(re.findall(r'[\u4e00-\u9fff]', text)), 'footnote_occurrences': len(refs), 'footnote_definitions': len(definitions)},
        'result': 'FINDINGS' if findings else 'CHECKED_INVARIANTS_PASS',
        'findings': findings,
    }

def init_project(path, title, profile, local_date):
    if path.exists() and (not path.is_dir() or any(path.iterdir())):
        raise ValueError('Refusing to overwrite a non-empty project directory')
    if local_date: date.fromisoformat(local_date)
    path.mkdir(parents=True, exist_ok=True)
    for name in ('00_管理', '01_材料', '02_研究', '03_正文', '04_审查', '05_交付'):
        (path/name).mkdir()
    templates = ROOT/'assets'/'templates'
    pairs = {'项目卡.md':'00_管理/项目卡.md', '来源登记.md':'02_研究/来源登记.md', 'sources.json':'02_研究/sources.json', '精读笔记.md':'02_研究/精读笔记.md', '检索与综述矩阵.md':'02_研究/检索与综述矩阵.md', '论证与引注表.md':'02_研究/论证与引注表.md', '论文正文.md':'03_正文/论文_v1.md', '反馈与修订.md':'04_审查/反馈与修订.md', '审稿报告.md':'04_审查/审稿报告.md', '交付检查.md':'05_交付/交付检查.md'}
    if profile == 'longform': pairs.update({'长篇批次.md':'00_管理/长篇批次.md', '图表数值与术语.md':'00_管理/图表数值与术语.md'})
    for a,b in pairs.items(): shutil.copyfile(templates/a,path/b)
    (path/'00_管理/决定记录.md').write_text('# 已确认决定\n\n| 编号/日期 | 决定及依据 | 影响范围 | 状态 |\n|---|---|---|---|\n',encoding='utf-8')
    (path/'00_管理/待核清单.md').write_text('# 待核清单\n\n| 位置 | 缺什么 | 影响的判断 | 补充路径 | 状态 |\n|---|---|---|---|---|\n',encoding='utf-8')
    (path/'00_管理/progress.json').write_text(json.dumps({'title':title,'profile':profile,'local_date':local_date,'state':'initialized','latest_manuscript':'03_正文/论文_v1.md','mechanical_audit':'not_run','semantic_review':'not_run','layout_review':'not_run','next_action':'read course requirements and materials'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    card=path/'00_管理/项目卡.md'
    card.write_text(card.read_text(encoding='utf-8').replace('# 论文项目卡','# 论文项目卡：'+title,1),encoding='utf-8')
    return {'project':str(path.resolve()),'state':'initialized','profile':profile,'files':len(list(path.rglob('*')))}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    sub=ap.add_subparsers(dest='command',required=True)
    p=sub.add_parser('init'); p.add_argument('path',type=Path); p.add_argument('--title',required=True); p.add_argument('--profile',choices=['course','longform'],default='course'); p.add_argument('--date',default=None)
    p=sub.add_parser('audit'); p.add_argument('path',type=Path); p.add_argument('--registry',type=Path); p.add_argument('--final',action='store_true'); p.add_argument('--check-files',action='store_true'); p.add_argument('--format',choices=['text','json'],default='text')
    a=ap.parse_args()
    try:
        if a.command=='init': result=init_project(a.path,a.title,a.profile,a.date); code=0
        else: result=audit(a.path,a.registry,a.final,a.check_files); code=int(bool(result['findings']))
        if getattr(a,'format','json')=='json': print(json.dumps(result,ensure_ascii=False,indent=2))
        else:
            print(result['result']); print(result['scope'])
            for f in result['findings']: print(f"[{f['severity']}] {f['code']} line={f.get('line','-')}: {f['message']}")
            print('NOT ASSESSED: '+', '.join(result['NOT_ASSESSED']))
        return code
    except (OSError, ValueError, TypeError, KeyError) as e:
        print('INPUT ERROR: '+str(e),file=sys.stderr); return 2

if __name__=='__main__': sys.exit(main())
