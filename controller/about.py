#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libs.handler import BaseHandler


class AboutHandler(BaseHandler):
    def get(self):
        self.render('about.html')
