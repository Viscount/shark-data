#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
import pymongo


class MongoConnector:
    if config.MONGO['user']:
        _client = pymongo.MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin'
            % (
                config.MONGO['user'],
                config.MONGO['passwd'],
                config.MONGO['host'],
                config.MONGO['port'],
            ),
            tz_aware=True
        )
    else:
        _client = pymongo.MongoClient(config.MONGO['host'], config.MONGO['port'], tz_aware=True)
    _db = _client.get_database(config.MONGO['db'])

    def __init__(self):
        pass

    @staticmethod
    def getClient():
        return MongoConnector._client
    @staticmethod
    def getDb():
        return MongoConnector._db

    def getCollections(self):
        return [str(x) for x in self.getDb().collection_names()]

    def getCollection(self, name):
        return self.getDb()[name]

    def dropCollection(self, name):
        pass


if __name__ == '__main__':
    mc = MongoConnector()
    print mc.getCollections()
    print mc.getCollection('Attach').find_one()
