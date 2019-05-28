import pymongo

connection = pymongo.MongoClient()

database = connection['data']

collection = database['gameData']