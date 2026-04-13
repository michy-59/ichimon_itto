import pandas as pd

df = pd.read_csv('prob.csv')
rc = len(df)
rc_u = len(df[['year', 'no']].drop_duplicates())

if rc == rc_u:
    print('OK')
    df = df.sort_values(['year', 'no'])
    df.to_csv('prob.csv',index=0)