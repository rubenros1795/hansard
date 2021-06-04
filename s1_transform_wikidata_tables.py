import pandas as pd
from glob import glob as gb
import os

filenames = [i for i in gb('/media/ruben/Elements/PhD/data/hansard/resources/wikidata-members/raw/*') if "Q" in i]

for fn in filenames:
    df = pd.read_csv(fn,sep='\t')
    year = int(df['?start'][0][:4])
    df.columns = ["mp_ref","mp","term_ref","term","constituency_ref","constituency","party_ref","party","start","election_ref","election","end","cause_ref","cause"]
    df['start'] = [str(x)[:10] for x in df['start']]
    df['end'] = [str(x)[:10] for x in df['end']]

    for c in "mp term constituency party election cause".split(' '):
        df[c] = [str(x).replace('@en','') for x in df[c]]
    fn_new = f"/media/ruben/Elements/PhD/data/hansard/resources/wikidata-members/reformatted/{year}-{os.path.split(fn)[-1][:-4]}.tsv"
    print(fn_new)
    df.to_csv(fn_new,index=False,sep='\t')