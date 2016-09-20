# -*- coding: utf-8 -*-

from model.project import Project
import random
import string
import os.path
import json


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.whitespace
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_symb(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

latin_mheg = [Project(branchName=random_string("branch",10), appId=random_string("appid",10),
                     scope=random_string("scope", 10), root = random_string("root", 10))]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/project.json")


# with open(file, 'w') as f:
#     f.write(json.dumps(test_data, default=lambda x: x.__dict__, indent = 2))
#
#
with open(file, 'w') as f:
    f.write(json.dumps({"mheg_positive": latin_mheg}, default=lambda x: x.__dict__, indent = 2))


