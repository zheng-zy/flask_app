# coding=utf-8
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


# 上下文处理器能让变量在所有模版中全局可以访问
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
