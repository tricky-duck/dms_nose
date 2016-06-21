__author__ = 'anna.matveeva'

from nose_config import *

#
# def setup_package():
#     global app
#     print(__name__, '__init__.py : teardown_package() =====================================')
#     app = set_app()
#

def teardown_package():
    global app
    print(__name__, '__init__.py : teardown_package() =====================================')
    app = stop_app()
