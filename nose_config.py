# -*- coding: utf-8 -*-

from time import sleep
from fixture.app import Application
import os.path
import json
import jsonpickle


config_file = None
config_file_name = "config_file.json"
app = None


def load_config(file_name="config_file.json"):
    global config_file
    if config_file is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        with open(config_file_path) as f:
            config_file = json.load(f)
    return config_file

def loads_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s" % file)) as f:
        return json.loads(f.read())

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s" % file)) as f:
        return json.load(f.read())

def set_app():
    global app
    web_config = load_config(config_file_name)['web']
    other_config = load_config(config_file_name)['other']
    if app is None or not app.is_valid():
        app = Application(browser=other_config['browser'])
        print ('SET_APP'), app
    app.session.ensure_login(web_config['username'], web_config['password'])
    return app

def stop_app():
    sleep(1)
    if app:
        app.session.ensure_logout()
        app.destroy()
    print ('STOP_APP'), app
    return app
