"""Immutable archive input and deterministic output helpers (standard library)."""
import csv, hashlib, json
from pathlib import Path
SHA256='51c66d4dcec9b6bc035d9a08e51d4a7b750615b6fc469be1d666e5d5693ebb05'
SIZE=17520509
COMMIT='2c6b485ae1c2bd296ad7d5e0eee4da4065535e57'
URL=f'https://raw.githubusercontent.com/nelson-liu/evaluating-verifiability-in-generative-search-engines/{COMMIT}/human_evaluation_annotations.jsonl'
def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(r): return json.dumps(r,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def load(path,check_identity=True):
    path=Path(path)
    if check_identity and (path.stat().st_size!=SIZE or digest(path)!=SHA256):
        raise ValueError('STOP: archive identity mismatch; preserve file and investigate provenance')
    records=[]
    with path.open(encoding='utf-8') as f:
        for line,text in enumerate(f,1):
            try:
                r=json.loads(text)
                if not isinstance(r,dict): raise ValueError('Expected JSON object')
            except (ValueError,UnicodeError) as e: raise ValueError(f'Invalid JSONL at line {line}: {e}') from e
            records.append((line,r))
    return records

def write_json(path,obj):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def write_csv(path,rows,fields=None):
    rows=list(rows);p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    fields=fields or (list(rows[0]) if rows else ['status'])
    with p.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
