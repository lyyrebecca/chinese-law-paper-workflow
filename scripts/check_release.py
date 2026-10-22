#!/usr/bin/env python3
"""Read-only checks for the sanitized distributable; not a legal-source audit."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEGAL_NAMES = {'LICENSE', 'NOTICE.md', 'CREDITS.md', 'THIRD_PARTY_NOTICES.md'}
REMOVED_METADATA = {'_store_meta.json', '_meta.json', '_skillhub_meta.json', '_icon.png', '_deltest.txt'}

def distributable_files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(x in {'.git','__pycache__','.venv','dist'} for x in p.relative_to(ROOT).parts) and p.suffix not in {'.pyc','.pyo'} and p.name != '.DS_Store')

def main():
    errors=[]
    files=distributable_files()
    manifest=json.loads((ROOT/'package-manifest.json').read_text(encoding='utf8'))
    expected={x['path']:x for x in manifest['files']}
    actual={p.relative_to(ROOT).as_posix():p for p in files if p.name!='package-manifest.json'}
    if set(expected)!=set(actual): errors.append('Package file set mismatch: '+str(sorted(set(expected)^set(actual))))
    for path,p in actual.items():
        if path not in expected:continue
        b=p.read_bytes(); entry=expected[path]
        if len(b)!=entry['bytes'] or hashlib.sha256(b).hexdigest()!=entry['sha256']:errors.append('Package checksum mismatch: '+path)
    source=json.loads((ROOT/'references/source-manifest.json').read_text(encoding='utf8'))
    source_paths={x['bundled_path'] for x in source['files']}
    actual_source={p.relative_to(ROOT).as_posix() for p in files if p.is_relative_to(ROOT/'references/source-library')}
    if source_paths!=actual_source:errors.append('Reference library file set mismatch')
    for entry in source['files']:
        p=ROOT/entry['bundled_path']
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256'] or p.stat().st_size!=entry['bytes']:errors.append('Reference checksum mismatch: '+entry['bundled_path'])
    # Known historical account tokens are encoded here to avoid publishing them as ordinary metadata.
    old_accounts=['zhang'+'ligong0826','Victor'+'Tran1023','matt'+'wang1230','Keize'+'-Tang','new'+'deme','Sheng'+' Chang','shawndeng'+'321']
    local_path=re.compile(r'/(?:Us' + r'ers|ho' + r'me)/[^/\s]+/')
    for p in files:
        rel=p.relative_to(ROOT).as_posix()
        if p.name in REMOVED_METADATA or p.suffix=='.skill':errors.append('Private metadata or opaque archive: '+rel)
        try:text=p.read_text(encoding='utf8')
        except UnicodeDecodeError:continue
        if local_path.search(text):errors.append('Personal absolute path: '+rel)
        if p.name in LEGAL_NAMES:continue
        for lineno,line in enumerate(text.splitlines(),1):
            if re.match(r'^\s*#?\s*Copyright\b',line,re.I):continue
            if any(account in line for account in old_accounts):errors.append(f'Historical identity outside legal attribution: {rel}:{lineno}')
    for name in ('SKILL.md','README.md'):
        text=(ROOT/name).read_text(encoding='utf8')
        if 'lyyrebecca' not in text or 'shirebeccaha' not in text:errors.append('Missing project contact: '+name)
    if [p.relative_to(ROOT).as_posix() for p in files if p.name=='SKILL.md'] != ['SKILL.md']:errors.append('Expected exactly one discoverable SKILL.md')
    print(json.dumps({'status':'PASS' if not errors else 'FAIL','files_checked':len(files),'reference_files_checked':len(source_paths),'errors':errors},ensure_ascii=False,indent=2))
    return bool(errors)

if __name__=='__main__':sys.exit(main())
