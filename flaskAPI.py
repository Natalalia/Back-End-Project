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
        print(games)
        gamesList1 = []
        for g in games:

            gamesList1.append({'id': str(g["_id"]), 'title': g["title"],
                               'description': g["description"], 'completion': g["completion"], 'levels': g["levels"]})

        return gamesList1


class GetAndPostGames(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        gamesList = db.gamesList
        games = db.player_games
        game_id = games.insert_one(json_data).inserted_id
        gamesList.insert({"id": json_util.dumps(game_id),
                          "title": json_data["title"]})
        leaderBoard = db.leaderboards
        leaderBoard.insert({"game_id": str(game_id), "leaderboard": []})
        return {"game_id": str(game_id)}

    def get(self):
        args = request.args
        id = args['id']
        games = db.player_games

        game = [g for g in games.find(
            {"_id": ObjectId(id)})]
        return {'id': str(game[0]["_id"]), 'title': game[0]["title"], 'description': game[0]["description"], 'completion': game[0]["completion"], 'levels': game[0]["levels"]}


class GetAndAddUsers(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        usersList = db.usersList
        users = db.users
        user_id = users.insert(json_data).inserted_id
        usersList.insert({'game_id': user_id, 'title': json_data['title']})
        return {'user_id': json_util.dumps(user_id)}

    def get(self):
        args = request.args
        id = args['id']
        users = db.users
        user = [i for i in users.find({'_id': ObjectId(id)})]
        return json_util.dumps(user)


class LeaderBoard(Resource):
    def get(self):
        args = request.args
        leaderboards = db.leaderboards
        leaderboard = [l for l in leaderboards.find(
            {"game_id": args['game_id']})]
        return {"leaderBoard": leaderboard[0]["leaderboard"]}

    def patch(self):
        json_data = request.get_json(force=True)
        game_id = json_data["game_id"]
        score = json_data["score"]
        username = json_data["username"]
        leaderboards = db.leaderboards
        leaderboards.update({"game_id": game_id}, {
                            "$push": {"leaderboard": {"score": score, "username": username}}})
        return "ok"


api.add_resource(LeaderBoard, '/leaderboards')
api.add_resource(GetAndAddUsers, '/users')
api.add_resource(GetAndPostGames, '/games')
api.add_resource(GetGamesList, '/gameslist')
app.register_blueprint(api_bp)
if __name__ == '__main__':
    app.run(debug=True)
