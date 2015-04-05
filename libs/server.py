# -*- coding: utf-8 -*-

import os
import logging

from pymongo import MongoClient
from tornado.web import Application
from tornado.escape import url_escape

import routes
from uimodule import uimodules
from libs.jinja import JinjaLoader

log = logging.getLogger('Main.BlogServer')


class BlogServer(Application):
    def __init__(self, options):

        loader = JinjaLoader(
            "templates",
            debug=options.debug)
        loader.env.globals['url_escape'] = url_escape

        app_settings = dict(
            template_loader=loader,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret=options.cookie_secret,
            xsrf_cookies=True,
            debug=options.debug,
            login_url="/login",
            ui_modules=uimodules
        )

        self.db = MongoClient(options.mongodb_host)[options.db_name]
        log.info("Connected to database %s:%s ...",
                 options.mongodb_host,
                 options.db_name)

        the_routes = routes.get(options)
        super(BlogServer, self).__init__(the_routes, **app_settings)
