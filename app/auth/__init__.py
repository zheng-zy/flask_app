#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/10/4.
from flask import Blueprint

# 下面两行代码有顺序要求
auth = Blueprint('auth', __name__)
from . import views
