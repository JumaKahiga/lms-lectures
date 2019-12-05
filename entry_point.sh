#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8


# export FLASK_APP=manage.py
echo "<<<<<<<< Database Setup >>>>>>>>>"

python3 -m flask db stamp heads
python3 -m flask db migrate
python3 -m flask db upgrade

echo "<<<<<<<< Database Setup Successfully >>>>>>>>>>>>>>>>>>"

python3 -m app.utilities.data_loader

echo "<<<<<<<< Seed data loaded Successfully >>>>>>>>>>>>>>>>>>"



python3 -m manage