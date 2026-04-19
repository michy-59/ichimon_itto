import pandas as pd

df = pd.read_csv('prob.csv')
df = df.sort_values(['year', 'no'])
df.to_csv('prob.csv',index=0)

df_u = df.groupby(['year', 'no'])['prob'].count().reset_index()
df_u = df_u.rename(columns={'prob': 'cnt'})
df_u = df_u[df_u['cnt'] > 1]


if len(df_u) == 0:
    print('OK')
else:
    print(df_u)