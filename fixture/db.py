# -*- coding: utf-8 -*-
import psycopg2
# from model.media import Media


class DbFixture:
    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password
        self.connection = psycopg2.connector.connect(host=host, port=port, database=name, user=user, password=password)
        self.connection.autocommit = True

    def destroy(self):
        self.connection.close()
