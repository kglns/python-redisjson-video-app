#!/bin/bash

export FLASK_APP=app.py

pkill -f "flask run"
flask run &
