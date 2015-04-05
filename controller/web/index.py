# -*- coding: utf-8 -*-

from libs.handler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html')
