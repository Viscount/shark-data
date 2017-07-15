#!/usr/bin/python
# -*- coding: utf-8 -*-


class Model:
    def __init__(self, connector):
        self.connector = connector
        # print connector


class MongoModel(Model):
    # 增
    def insert(self, collectionName, data):
        collection = self.connector.getCollection(collectionName)
        return collection.insert_one(data).inserted_id

    def inserts(self, collectionName, dataList):
        collection = self.connector.getCollection(collectionName)
        return collection.insert_many(dataList).inserted_ids

    # 删
    def remove(self, collectionName, filter, multi=False):
        collection = self.connector.getCollection(collectionName)
        if multi:
            return collection.remove(filter)
        else:
            item = collection.find_one(filter)
            if item:
                return collection.remove(item)
            else:
                return None

    # 改
    def update(self, collectionName, filter, data, multi=False):
        collection = self.connector.getCollection(collectionName)
        return collection.update(filter, {'$set': data}, multi=multi)

    # 查
    def find(self, collectionName, filter, multi=False):
        collection = self.connector.getCollection(collectionName)
        if multi:
            result = []
            for cursor in collection.find(filter):
                result.append(cursor)
            return result
        else:
            return collection.find_one(filter)


def tupleGroup(l):
    return '(%s)' % ','.join(l)


def dictGroup(d, s='and'):
    seq = []
    for x in d:
        if isinstance(d[x], list):
            list_str = "(" + repr(d[x])[1:-1] + ")"
            sub_clause = ("%s in %s" % (x, list_str))
            seq.append(sub_clause)
        elif isinstance(d[x], dict):
            for operator in d[x]:
                if operator == "$gt":
                    sub_clause = ("%s > %s" % (x, repr(str(d[x][operator]))))
                elif operator == "$lt":
                    sub_clause = ("%s < %s" % (x, repr(str(d[x][operator]))))
                elif operator == "$nn":
                    if d[x][operator]:
                        sub_clause = ("%s is null" % x)
                    else:
                        sub_clause = ("%s is not null" % x)
                if d[x][operator]is not None:
                    seq.append(sub_clause)
        else:
            sub_clause = ("%s = %s" % (x, repr(str(d[x]))))
            seq.append(sub_clause)
    return (' %s ' % s).join(seq)


class MySQLModel(Model):
    # 增
    def insert(self, table, data):
        key = tupleGroup([i for i in data])
        val = tupleGroup([repr(data[i]) for i in data])
        sql = 'insert into %s %s values %s;' % (table, key, val)
        res = self.connector.execute(sql)
        return res

    def inserts(self, table, dataList, inTurn = False):
        res = []
        if inTurn:
            for i in dataList:
                res.append(self.insert(table, i))
            return res
        else:
            rows = self.connector.getRows(table)
            key = tupleGroup(rows)
            r = rows[0]
            val = tupleGroup([
                tupleGroup([
                    repr(data.get(r)) 
                    if data.get(r) != None 
                    else 'NULL' 
                    for r in rows
                ]) for data in dataList
            ])[1:-1]
            sql = 'insert into %s %s values %s;' % (table, key, val)
            res = self.connector.execute(sql)
            return res

    # 删
    def remove(self, table, filter, multi=False):
        where = \
            'where ' + dictGroup(filter) \
            if filter else ''
        limit = '' if multi else 'limit 1'
        sql = 'delete from %s %s %s;' % (table, where, limit)
        res = self.connector.execute(sql)
        return res

    # 改
    def update(self, table, filter, data):
        cet = \
            'set ' + dictGroup(data, ',') \
            if data else ''
        where = \
            'where ' + dictGroup(filter) \
            if filter else ''
        sql = 'update %s %s %s;' % (table, cet, where)
        # print sql
        res = self.connector.execute(sql)
        return res

    # 查
    def find(self, table, filter={}, multi=False):
        where = \
            'where ' + dictGroup(filter) \
            if filter else ''
        limit = '' if multi else 'limit 1'
        sql = 'select * from %s %s %s;' % (table, where, limit)
        res = self.connector.execute(sql)
        return res


if __name__ == '__main__':

    # MongoDB 模块测试

    import mongo
    mc = mongo.MongoConnector()
    mm = MongoModel(mc)
    # print mm.insert('tjuser', {'age': 1, 'name': 'lee'})
    print mm.find('Clazz', {'name': '英音晨读－斯内普的故事'})
    # print mm.remove('tjuser',  {'name': 'lee'})
    # print mm.update('tjuser', {'name': 'lee'}, {'name': 'leo'}, True)
    # print mm.inserts('tjuser', [{'name': 'one'}, {'name': 'two'}])

    # Mysql 模块测试

    # import mysql
    # mc = mysql.MySQLConnector()
    # mm = MySQLModel(mc)
    # print mm.find('user', multi=True)
    # print mm.find('user', {'age': 64, 'name': 'leo8'})
    # print mm.find('user', {'name': 'lee'}, True)

    # print mm.insert('tjuser', {'name': 'freshman', 'age': 18})

    # print mm.inserts('tjuser', [{
    #     'name': 'leo%d' % x,
    #     'age': x * x
    # } for x in range(10)])

    # print mm.remove('tjuser', {'name': 'leo0'})
    # print mm.remove('tjuser', {'name': 'leo1'}, True)

    # print mm.update('tjuser', {'name': 'leo2'}, {'name': 'lee', 'age': 25})

