#!usr/bin/env python
# coding=utf-8
# Created by zhezhiyong@163.com on 2016/11/16.

import re
import unittest

from flask import url_for

from app import create_app, db
from app.models import User, Role


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Stranger' in response.get_data(as_text=True))

    def test_register_and_login(self):
        # 注册新用户
        response = self.client.post(url_for('auth.register'), data={
            'email': '595008292@qq.com',
            'username': '595008292',
            'password': '123',
            'password2': '123'
        })
        self.assertTrue(response.status_code == 302)

        # 使用新注册的账户登陆
        response = self.client.post(url_for('auth.login'), data={
            'email': '595008292@qq.com',
            'password': '123'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue(re.search('Hello,\s+595008292!', data))
        self.assertTrue('You have not confirmed your account yet' in data)

        # 发送确认令牌
        user = User.query.filter_by(email='595008292@qq.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get(url_for('auth.confirm', token=token, follow_redirects=True))
        data = response.get_data(as_text=True)
        self.assertTrue('You have confirmed your account' in data)

        # 退出
        response = self.client.get(url_for('auth.logout'), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('You have been logged out' in data)
