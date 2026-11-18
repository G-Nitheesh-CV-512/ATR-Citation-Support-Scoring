import sys,argparse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.data_loader import load,write_json,write_csv,digest,COMMIT,URL
from src.validation import validate
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--out',default='results');a=p.parse_args()
    r=load(a.data);counts,labels,audit,_=validate(r)
    out=Path(a.out);write_json(out/'logs/dataset_validation.json',dict(sha256=digest(a.data),size_bytes=Path(a.data).stat().st_size,source=URL,commit=COMMIT,counts=counts,labels=dict(labels),invalid_jsonl=0))
    write_csv(out/'tables/dataset_structure.csv',[dict(measure=k,value=v) for k,v in counts.items()])
    write_csv(out/'tables/record_audit.csv',audit);print(counts)
