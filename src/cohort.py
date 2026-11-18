"""Frozen all-system intersections; duplicates never become independent generations."""
from collections import defaultdict
from .data_loader import canonical
SYSTEMS=('bing_chat','neeva','perplexity','you')
def resolve(records,mode):
    groups=defaultdict(list)
    for line,r in records:groups[r['id']].append((line,r))
    selected=[];audit=[]
    for rid,rows in sorted(groups.items()):
        unique={}
        for line,r in rows:unique.setdefault(canonical(r),(line,r))
        reason='retained'
        if mode=='unique_raw' and len(rows)>1:reason='repeated_id_excluded'
        if mode=='identical' and len(unique)>1:reason='conflicting_records_excluded'
        if len({r['response'] for _,r in rows})>1:reason='conflicting_response_text'
        if reason=='retained':selected.extend(rows if mode=='unique_raw' else unique.values())
        for line,r in rows:audit.append({'line':line,'id':rid,'raw_group_size':len(rows),
             'distinct_records':len(unique),'mode':mode,'disposition':reason,
             'representative_line':unique[canonical(r)][0]})
    return selected,audit

def common_cohort(selected,parsed,mode):
    groups=defaultdict(list)
    for line,r in selected:groups[(r['query'],r['system_name'])].append((line,r))
    eligible={}
    for key,rows in groups.items():
        if any(parsed[line][1] for line,r in rows):continue
        if mode!='distinct_mean' and len(rows)!=1:continue
        if len({r['id'] for line,r in rows})!=1:continue
        eligible[key]=rows
    queries=sorted(q for q in {q for q,s in groups} if all((q,s) in eligible for s in SYSTEMS))
    return queries,{(q,s):eligible[q,s] for q in queries for s in SYSTEMS}
