#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/17.

from flask import jsonify

from . import api
from .. import mongodb


@api.route('/books/')
def get_books():
    # id =  mongodb.db.book.insert({'test':1})
    books = mongodb.db.Book.find({})
    for book in books:
        print book
    return jsonify({
        'code': str(id)
    })
