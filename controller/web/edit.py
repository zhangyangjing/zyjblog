#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.options import options
from libs.handler import AuthHandler


class EditHandler(AuthHandler):
    def get(self, article_id=None):
        if options.admin_user != self.current_user:
            self.redirect('/login')
        else:
            article_id = (article_id is None and [""] or [article_id])[0]
            self.render('edit.html', article_id=article_id)
