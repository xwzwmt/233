import pymongo
client=pymongo.MongoClient('localhost',27017)
ershouche=client['ershouche']
infoX=ershouche['infoX']
content=infoX.find({"area":{'$regex':'上海'}}).limit(1000)
for i in content:
    print(i)