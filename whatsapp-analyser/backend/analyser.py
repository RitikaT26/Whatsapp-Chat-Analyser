import pandas as pd

def analyse(df):
    df= df.dropna()
    df['date']= pd.to_datetime(df['date'])
    ld= df['date'].max()
    lw= ld - pd.Timedelta(days=6)
    dfw= df[df['date'] >= lw]
    au= dfw.groupby("date")['user'].nunique()

    fs= df.groupby('user')['date'].min()
    nu= fs[fs >= lw].groupby(fs).count()
    ud= dfw.groupby('user')['date'].nunique()
    cu= ud[ud >= 4].index.tolist()

    return {'active_users': au.to_dict(), 'new_users': nu.to_dict(), 'consistent_users': cu}
