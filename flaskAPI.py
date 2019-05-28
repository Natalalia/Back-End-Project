from flask import Flask, request, Blueprint
from flask_restful import Resource, Api, reqparse, url_for
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
client = MongoClient()
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


api.add_resource(GetAndPostGames, '/games')
api.add_resource(GetGamesList, '/gameslist')
app.register_blueprint(api_bp)
if __name__ == '__main__':
    app.run(debug=True)
