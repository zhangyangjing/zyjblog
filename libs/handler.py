# -*- coding: utf-8 -*-

from tornado.web import authenticated
from tornado.web import RequestHandler

from model import user


class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db


class AuthHandler(BaseHandler):
    @authenticated
    def prepare(self):
        pass

    def set_current_user(self, user_name):
        self.set_secure_cookie('un', user_name)
        self.current_user = None

    def clear_current_user(self):
        self.clear_cookie('un')
        self.current_user = None

    def get_current_user(self):
        user_name = self.get_secure_cookie('un')
        if user_name is None:
            return None
        return user.get_user(self, user_name)


class ServiceHandler(BaseHandler):
    pass


class WebHandler(AuthHandler):
    pass


class AjaxHandler(AuthHandler):
    pass
