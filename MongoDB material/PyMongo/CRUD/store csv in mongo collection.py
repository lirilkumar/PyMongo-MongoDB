import json
from Connection import ConnectionMongo
import pandas

con=ConnectionMongo()
connection=con.returnCollection('Trial')
connection.drop()

# insert csv in collection

sample_data_df=pandas.read_csv('Reservoir E.csv',header=0,parse_dates=True)
records = json.loads(sample_data_df.T.to_json()).values()
connection.insert(records)

print('success')

