#!/usr/bin/env python3
"""Rebuild public file manifests after deliberate release edits."""
import hashlib
import json
from pathlib import Path
from check_release import ROOT, distributable_files

NAMES={'S01':'law-paper-writing','S02':'law-paper-writing-skill','S03':'Law-Thesis-Template-Library','S04':'lawpaper-skill','S05':'legal-citation','S06':'legal-paper-framework-humanizer-zh','S07':'legal-writing-style','S08':'monograph-writing','S09':'literature-relay','S10':'social-science-paper-writing-skill'}
def digest(p):
    data=p.read_bytes()
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def write(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def main():
    records=[]
    for p in distributable_files():
        if not p.is_relative_to(ROOT/'references/source-library'):continue
        rel=p.relative_to(ROOT/'references/source-library'); sid=rel.parts[0]
        records.append({'source_id':sid,'source_skill':NAMES[sid],'source_relative_path':Path(*rel.parts[1:]).as_posix(),'bundled_path':p.relative_to(ROOT).as_posix(),**digest(p)})
    write(ROOT/'references/source-manifest.json',{'snapshot_date':'2026-10-22','scope':'Sanitized distributed reference files; not byte-identical original snapshots. Copyright notices preserved.','files':records})
    write(ROOT/'package-manifest.json',{'name':'chinese-law-paper-workflow','version':'1.0.1','date':'2026-10-22','maintainer':'lyyrebecca','files':[{'path':p.relative_to(ROOT).as_posix(),**digest(p)} for p in distributable_files() if p.name!='package-manifest.json']})
    print(f'Manifests rebuilt: {len(records)} reference files.')
if __name__=='__main__':main()
