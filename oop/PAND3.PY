import pandas as pd
data={
    "name":["Ann","Emma","jose","Riya","Rose","Liya","Rahul","Jiya"],
    "marks":[34,40,5,78,90,24,78,80,]
}

df=pd.DataFrame(data)

print(df.loc[0],df.loc[1])
