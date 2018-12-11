import pymongo
client = pymongo.MongoClient("mongodb://127.0.0.1:27117/ace")
mdb = client.ace
no_devices = mdb.device.count()
print no_devices
