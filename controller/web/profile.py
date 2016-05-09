#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tornado.options import options
from libs.handler import BaseHandler


class ProfileHandler(BaseHandler):
    def get(self):
        profile_path = os.path.join(options.static_dir, 'mix/profile.pdf')
        with open(profile_path) as f:
            self.set_header("Content-Type", 'application/pdf')
            self.finish(f.read())
