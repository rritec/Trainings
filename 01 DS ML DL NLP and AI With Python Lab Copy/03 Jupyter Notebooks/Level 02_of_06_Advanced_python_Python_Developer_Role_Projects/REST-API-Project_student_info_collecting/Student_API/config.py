import pymongo
myclient = pymongo.MongoClient(u"mongodb://localhost:27017")
mydb = myclient["rritec_20191109"]
coll_name = 'frameworks'
mycol = mydb[coll_name]