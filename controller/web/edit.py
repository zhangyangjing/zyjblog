#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libs.handler import BaseHandler


class EditHandler(BaseHandler):
    def get(self, article_id=None):
        article_id = (article_id is None and [""] or [article_id])[0]
        self.render('edit.html', article_id=article_id)
