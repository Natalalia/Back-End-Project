from flask import Flask, request, Blueprint
from flask_restful import Resource, Api, reqparse, url_for
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
client = pymongo.MongoClient(
    "mongodb+srv://alpha1:alpha1@cluster0-w2dum.mongodb.net/test?retryWrites=true")
db = client.test



db = client.games
app = Flask(__name__)
CORS(app)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class GetGamesList(Resource):
    def get(self):
        gamesList = db.player_games
        games = gamesList.find({})
        
        gamesList1 = []
        for g in games :
            gamesList1.append({'id': str(g["_id"]), 'title': g["title"], 'description': g["description"], 'completion': g["completion"], 'levels': g["levels"]})
        return gamesList1


class GetAndPostGames(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        gamesList = db.gamesList
        leaderBoard = db.leaderBoard
        games = db.player_games
        game_id = games.insert_one(json_data).inserted_id
        gamesList.insert({"id": json_util.dumps(game_id),
                          "title": json_data["title"]})
        leaderBoard.insert({ json_util.dumps(game_id): json_data["title"]})
        return {"game_id": str(game_id)}

    def get(self):
        args = request.args
        id = args['id']
        games = db.player_games
        
        game = [g for g in games.find(
            {"_id": ObjectId(id)})]
        return {'id': str(game[0]["_id"]), 'title': game[0]["title"], 'description': game[0]["description"], 'completion': game[0]["completion"], 'levels': game[0]["levels"]}

class GetAndAddLeaderBoards(Resource):
    def get(self):
        json_data = request.get_json(force=True)
        leaderBoard = db.leaderBoard
        return leaderBoard.find({})


class GetAndAddUsers(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        usersList = db.usersList
        users = db.users
        user_id = users.insert(json_data).inserted_id
        usersList.insert({'game_id': user_id, 'title': json_data['title']})
        return {'user_id':json_util.dumps(user_id)}

    def get(self):
        args = request.args
        id = args['id']
        users = db.users
        user = [i for i in users.find({'_id': ObjectId(id)})]
        return json_util.dumps(user)



api.add_resource(GetAndLeaderBoards, '/leaderboards')
api.add_resource(GetAndAddUsers, '/users')
api.add_resource(GetAndPostGames, '/games')
api.add_resource(GetGamesList, '/gameslist')
app.register_blueprint(api_bp)
if __name__ == '__main__':
    app.run(debug=True)
