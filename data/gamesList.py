import pymongo

connection = pymongo.MongoClient()

database = connection['data']

gamesList = database['gamesList']

games = {
    'games': [{ 'name': 'game1', 'id': 'game1' }, { 'name': 'game2', 'id': 'game2' }]
}

gamesList.insert_one(games)