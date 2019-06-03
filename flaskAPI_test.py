from flaskAPI import app, db
from flask import json
from assertpy import assert_that


def test_get_games_list():
    response = app.test_client().get('/gameslist')

    data = json.loads(response.get_data(as_text=True))
    print(data)

    assert response.status_code == 200
    completion = data[0]["completion"]
    levels = data[0]["levels"]
    title = data[0]["title"]
    assert_that(completion).is_not_empty()
    assert_that(levels).is_not_empty()
    assert_that(title).is_not_empty()


def test_post_game():
    test_game = {
        "title": "tonys test game",
        "description": "this is a test game to seed the database",
        "completion": "well done you have completed the game",
        "levels": [
            {
                "wincondition": "text",
                "mainclue": "just write hello",
                "clue2": "nothing",
                "clue3": "nothing again",
                "wintext": "you have won this level",
                "windata": "hello"
            },
            {
                "wincondition": "text",
                "mainclue": "just write hello",
                "clue2": "nothing",
                "clue3": "nothing again",
                "wintext": "you have won this level",
                "windata": "hello"
            }
        ]
    }

    response = app.test_client().post('/games',  json=test_game)

    data = json.loads(response.get_data(as_text=True))
    print(data)

    assert response.status_code == 200
    print(data)
