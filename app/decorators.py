#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/10/28.


"""
检查用户权限的自定义修饰器
"""

from functools import wraps

from flask import abort
from flask_login import current_user

from .models import Permisssion


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required(Permisssion.ADMINISTER)(f)
