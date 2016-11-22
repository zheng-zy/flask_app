#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/17.

import pymongo
from flask import render_template
from pymongo.collection import ObjectId

from . import book
from .. import mongodb


@book.route('/')
def index():
    books = mongodb.db.Book.find({})
    return render_template('book/book.html', books=books)


@book.route('/info/<id>')
def info(id):
    book = mongodb.db.Book.find_one_or_404({'_id': ObjectId(id)})
    bookinfos = mongodb.db.BookInfo.find({'book_id': ObjectId(id)}).sort([{'sort', pymongo.ASCENDING}]).skip(0).limit(
        100)
    return render_template('book/bookinfo.html', books=[book], bookinfos=bookinfos, book=book)


@book.route('/chapter/<id>')
def chapter(id):
    bookinfo = mongodb.db.BookInfo.find_one_or_404({'_id': ObjectId(id)})
    return render_template('book/chapter.html', bookinfo=bookinfo)
