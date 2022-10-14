from flask import Flask, request
from pydantic import ValidationError
from models import Video, User
from redis_om import Migrator

app = Flask(__name__)

# CRUD methods
# Create a new video.
@app.route("/video/new", methods=["POST"])
def create_video():
    try:
        print(request.json)
        new_video = Video(**request.json)
        new_video.save()
        return new_video.pk

    except ValidationError as e:
        print(e)
        return "Bad request.", 400

# Create a new user.
@app.route("/user/new", methods=["POST"])
def create_user():
    try:
        print(request.json)
        new_user = User(**request.json)
        new_user.save()
        return new_user.pk

    except ValidationError as e:
        print(e)
        return "Bad request.", 400

# Create a RediSearch index for instances of the models.
Migrator().run()
