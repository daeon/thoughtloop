#!/usr/bin/env python3
"""Validate standalone pack format and test-fixture coverage. Python stdlib only."""
from pathlib import Path
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]


def fail(msg):
    print('ERROR:',msg,file=sys.stderr)
    raise SystemExit(1)


def frontmatter(path):
    s=path.read_text(encoding='utf-8')
    if not s.startswith('---\n'):
        fail(f'{path}: missing YAML frontmatter')
    chunks=s.split('---',2)
    if len(chunks)<3 or not chunks[2].strip():
        fail(f'{path}: empty or malformed body')
    fields={}
    for line in chunks[1].splitlines():
        line=line.strip()
        if not line: continue
        if ':' not in line: fail(f'{path}: malformed line {line!r}')
        k,v=line.split(':',1)
        fields[k.strip()]=v.strip()
    return fields,chunks[2]


def main():
    files=sorted((ROOT/'skills').glob('*/SKILL.md'))
    if not files: fail('no skills found')
    names=set()
    bodies={}
    for f in files:
        meta,body=frontmatter(f)
        n=meta.get('name','')
        desc=meta.get('description','')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',n):fail(f'{f}: invalid name')
        if n!=f.parent.name:fail(f'{f}: name and path mismatch')
        if len(n)>64 or not (1<=len(desc)<=1024):fail(f'{f}: name/description length')
        if n in names:fail(f'duplicate skill {n}')
        for heading in ['## Procedure','## Output']:
            if heading not in body and not (heading=='## Output' and '## Result states' in body):
                fail(f'{f}: missing {heading}')
        names.add(n)
        bodies[n]=body
    # Prevent latent skill-to-skill requirements (cross-name skill mentions in instructions).
    for n,body in bodies.items():
        for other in names-{n}:
            if re.search(r'\b'+re.escape(other)+r'\b',body):
                fail(f'{n}: references independent skill {other}')
        if any(marker in body.casefold() for marker in ['invoke another skill','run another skill as prerequisite','depend on a skill library']):
            fail(f'{n}: possible dependency language')
    agent_files=sorted((ROOT/'agents/claude').glob('*.md'))
    if not agent_files:fail('no agents')
    for f in agent_files:
        meta,body=frontmatter(f)
        if meta.get('name')!=f.stem or not meta.get('description'):
            fail(f'{f}: invalid agent metadata')
        if not ('read-only' in body.lower() or 'do not modify' in body.lower()):
            fail(f'{f}: missing read-only boundary')
    cases=[json.loads(line) for line in (ROOT/'evals/cases.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    if len({c['id'] for c in cases})!=len(cases):fail('duplicate eval ID')
    for c in cases:
        if c['skill'] not in names or not isinstance(c['should_trigger'],bool) or not c['must_observe']:
            fail(f"invalid fixture: {c['id']}")
    for n in names:
        found={c['should_trigger'] for c in cases if c['skill']==n}
        if found!={True,False}:fail(f'{n}: missing positive/negative fixtures')
    assert (ROOT/'AGENTS.md').read_text()==(ROOT/'CLAUDE.md').read_text()
    print(f'PASS: {len(names)} independent skills; {len(agent_files)} self-contained agents; {len(cases)} eval fixtures; zero cross-skill dependencies')

if __name__=='__main__':main()
