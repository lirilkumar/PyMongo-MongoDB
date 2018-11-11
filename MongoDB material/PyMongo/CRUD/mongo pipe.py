import pandas
from Connection import ConnectionMongo

con=ConnectionMongo()
connection=con.returnCollection('Trial')

pipe=[
    {"$match":{"Precipitation":{"$gt":0}}},
    {"$sample":{"size":1000}},
    # {"$addFields":{"pre":0}},     #new 3.4 version
    {"$project":{"_id":0,"Volume":1}},
    {"$skip":1},
    {"$group": {"_id": "$Volume", "count": {"$sum": 1}}},
    {"$sort": {"count": 1}},
    {"$group": {"_id": "$count", "count": {"$sum": 1}}},
    {"$project": {"_id": 0, "count": 1}},
    {"$sort": {"count": -1}},
    {"$limit":2},
    # {"$count":1}                  #new 3.4 version
    # {"$out":"output_of_pipe"}     #enable to save to collection
]
print(list(connection.aggregate(pipe)))