import pymongo

connection = pymongo.MongoClient()

database = connection['data']

collection = database['gameData']

gameStructure = {    
    'title': 'game 1!',
    'levels': {
        '0': {
            'mainClue': "Welcome to my game, type 'start' to enter the game!",
            'hint1': 'Name a yellow fruit',
            'hint2': 'omfg youre dumb',
            'answer': 'start',
            'winCond': 'string'
        },
        '1': {
            'mainClue': 'Solve this riddle: what fruit is yellow?',
            'hint1': 'its a funny shape',
            'hint2': 'bananas dumb ass!',
            'answer': 'bananas',
            'winCond': 'string'
        },
        '2': {
            'mainClue': 'Solve this riddle: what fruit is yellow?',
            'hint1': 'its a funny shape',
            'hint2': 'bananas dumb ass!',
            'answer': '52.000,13.000',
            'winCond': 'gps'
        },
        '3': {
            'mainClue': 'You completed the challenge!',
            'hint1': 'Name a yellow fruit',
            'hint2': 'omfg youre dumb',
            'answer': 'banflaskdbanas',
            'winCond': 'string'
        }
    }   
}

collection.insert_one(gameStructure)


collection2 = database['gamesList']

games = {
    'games': [{ 'name': 'game1', 'id': 'game1' }, { 'name': 'game2', 'id': 'game2' }]
}

collection2.insert_one(games)