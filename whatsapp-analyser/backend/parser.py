import re
import pandas as pd

def parsechat(fp):
    pat= r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}) - (.*?): (.*)"
    data= []

    with open(fp, encoding= "utf-8") as f:
        for l in f:
            m= re.match(pat, l)
            if m:
                d, t, u, msg = m.groups()
                data.append([d,t,u,msg])

    df = pd.DataFrame(data, columns=["date", "time", "user", "message"])
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    return df