import pandas
from Connection import ConnectionMongo

con=ConnectionMongo()
connection=con.returnCollection('Trial')

cur=connection.find({'Volume':{"$lt":160}},{'_id':0})

df=pandas.DataFrame((list(cur)))
print(df.head(2))
df.to_csv('output.csv',index=False)

