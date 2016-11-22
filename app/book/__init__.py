#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/17.

from flask import Blueprint

book = Blueprint('book', __name__)

from . import views
