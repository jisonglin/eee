import pandas as pd

d={}
df = pd.read_csv('C:\\Users\\Admin\\Desktop\\test.csv')
data = df.index.values

for i in data:
   d.update({df.iloc[i,0]:df.iloc[i,1]})

for key in d:
    print("UPDATE res_tz_line SET use_date='{0}' WHERE line_id='{1}';\n".format(d[key],key))
