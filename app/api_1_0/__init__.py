#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/9.

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, books, comments
