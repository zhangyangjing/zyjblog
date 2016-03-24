#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import sha512
from tornado.options import options
from libs.handler import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        if self.current_user == options.admin_user:
            self.redirect('/')
        else:
            self.render('login.html')

    def post(self):
        pswd = self.get_argument('pswd')
        path = self.get_argument('next', '/')
        if sha512(pswd).hexdigest() == options.admin_pswd:
            self.set_current_user(options.admin_user)
            self.redirect(path)
        else:
            self.render('login.html', alert='wrong password')


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_current_user()
        self.render('logout.html')
