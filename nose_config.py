# -*- coding: utf-8 -*-

from time import sleep
from fixture.app import Application
from fixture.db import DbFixture
import os.path
import json
import jsonpickle


config_file = None
config_file_name = "config_file.json"
app = None
db = None


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

def set_app():
    global app
    web_config = load_config(config_file_name)['web']
    ui_config = load_config(config_file_name)['ui']
    if app is None or not app.is_valid():
        app = Application(browser=ui_config['browser'], baseUrl=web_config['baseUrl'],
                          width=ui_config['width'], height=ui_config['height'])
        print('starting application ', app)
    app.session.ensure_login(web_config['username'], web_config['password'])
    return app

def set_db():
    global db
    db_config = load_config(config_file_name)['db']
    db = DbFixture(host=db_config['host'], port=db_config['port'], name=db_config['name'], user=db_config['user'],
                   password=db_config['password'])
    print('starting data base ', db)
    return db

def stop_app():
    sleep(1)
    if app:
        app.session.ensure_logout()
        app.destroy()
    print ('STOP_APP'), app
    return app

def stop_db():
    db.destroy()
    print('stopping data base ', db)
    return db

def check_ui():
    return load_config(config_file_name)['ui']['check_ui'] == 'True'

def write_generated_data(file_path, data_list):
    with open(file_path, "w") as f:
        jsonpickle.set_encoder_options("simplejson", indent=2, ensure_ascii=False)
        f.write(jsonpickle.encode(data_list))
