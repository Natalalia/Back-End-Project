# Back-End-Project

## Overview

This is the Back End of the final project. 

Front End Repo: https://github.com/Natalalia/Plunder-Front-End

## Set up

Create virtual environment:

```
python3 -m venv nameofrunningfile
```

Activate virtual environment:

```
source nameofrunningfile/bin/activate
```

### Install dependencies

```
pip install Flask
```

```
pip install Flask-RESTful
```

```
pip install mongoengine
```

If requirements.txt already created just need to run `pip install -r requirements.txt` and all dependencies indicated in the file will be installed.

### Run the server

```
python3 index.py
```

### Run mongoDB

```
sudo service mongod start
```

### Install pip

```
sudo apt install python3-pip
```

### Install pipenv

```
sudo pip3 install pipenv


```

## Available endpoints

### /games

#### GET

/games?id=ndjksahdsauu38hjds

returns a game object with the following format

```js
{"title":"tonys test game",
"description":"this is a test game to seed the database","completion":"well done you have completed the game","levels":[{"wincondition":"text",
																																																												"mainclue":"just write hello",
																																																												"clue2":"nothing",
																																																												"clue3":"nothing again",
																																																												"wintext":"you have won this level","windata":"hello"},{"wincondition":"text",
																																																												"mainclue":"just write hello",
																																																												"clue2":"nothing",
																																																												"clue3":"nothing again",
																																																												"wintext":"you have won this level","windata":"hello"}]
```

#### POST

/games

post a game in the previous format , retuns the new game id

##/leaderboards

#### GET

returns a leaderboard object in the following format

{game_id,
levels:[]}

#### PATCH

accepts a body of {game_id:,
score:123,
username:}

## Contributors
*Authors*:
 - Kyle https://github.com/kyle974
 - Natalia https://github.com/Natalalia
 - Rob Clegg https://GitHub.com/Roberto198
 - Sam Wood https://github.com/sam90423
 - Tony Morris https://github.com/TonyDMorris
