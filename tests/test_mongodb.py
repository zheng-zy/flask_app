#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/18.
import unittest

from pymongo import ASCENDING
from pymongo import MongoClient
from pymongo.collection import ObjectId


class MongoDBTestCase(unittest.TestCase):
    def setUp(self):
        self.db = MongoClient('127.0.0.1').books
        self.collection = self.db.books
        self.book = self.collection.Book
        self.book_info = self.collection.BookInfo

    def tearDown(self):
        # self.db.close()
        pass

    def test_query_book(self):
        count = self.book.find({'_id': ObjectId("582e5fbed77ab35e18a1c8e1")}).count()
        self.assertTrue(1, count)

    def test_query_bookinfo(self):
        count = self.book_info.find({'book_id': ObjectId("582e5fbdd77ab35e18a1c8db")}).sort(
            [{'sort', ASCENDING}]).skip(0).limit(100).count()
        self.assertTrue(100, count)
