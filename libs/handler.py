# -*- coding: utf-8 -*-

from tornado.web import authenticated
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def md(self):
        return self.application.md

    def set_current_user(self, user_name):
        self.set_secure_cookie('un', user_name)
        self.current_user = None

    def clear_current_user(self):
        self.clear_cookie('un')
        self.current_user = None

    def get_current_user(self):
        return self.get_secure_cookie('un')


class AuthHandler(BaseHandler):
    @authenticated
    def prepare(self):
        pass


class ServiceHandler(BaseHandler):
    pass


class WebHandler(AuthHandler):
    pass


class AjaxHandler(AuthHandler):
    pass
