from flask import Flask, request, Blueprint
from flask_restful import Resource, Api, reqparse, url_for
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

client = pymongo.MongoClient(
    "mongodb+srv://alpha1:alpha1@cluster0-w2dum.mongodb.net/test?retryWrites=true")
db = client.test



db = client.games
app = Flask(__name__)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class GetGamesList(Resource):
    def get(self):
        gamesList = db.gamesList
        games = gamesList.find({})
        return json_util.dumps(games)


class GetAndPostGames(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        gamesList = db.gamesList
        games = db.player_games
        game_id = games.insert_one(json_data).inserted_id
        gamesList.insert({"id": game_id,
                          "title": json_data["title"]})
        return json_util.dumps({"game_id": game_id})

    def get(self):
        args = request.args
        id = args['id']
        games = db.player_games
        game = [i for i in games.find(
            {"_id": ObjectId(id)})]
        return json_util.dumps(game)

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




api.add_resource(GetAndAddUsers, '/users')
api.add_resource(GetAndPostGames, '/games')
api.add_resource(GetGamesList, '/gameslist')
app.register_blueprint(api_bp)
if __name__ == '__main__':
    app.run(debug=True)
