# -*- coding: utf-8 -*-

import logging

from pymongo import MongoClient
from tornado.web import Application
from tornado.escape import url_escape

import routes
from uimodule import uimodules
from libs.jinja import JinjaLoader
from libs.markdown import Markdown

log = logging.getLogger('Main.BlogServer')


class BlogServer(Application):
    def __init__(self, options):

        loader = JinjaLoader(
            "templates",
            debug=options.debug)
        loader.env.globals['url_escape'] = url_escape

        settings = dict(
            template_loader=loader,
            static_path=options.static_dir,
            cookie_secret=options.cookie_secret,
            xsrf_cookies=False,
            debug=options.debug,
            login_url="/login",
            ui_modules=uimodules
        )

        self.md = Markdown(extras=["fenced-code-blocks"])
        self.db = MongoClient(options.mongodb_host)[options.db_name]
        log.info("Connected to database %s:%s ...",
                 options.mongodb_host,
                 options.db_name)

        the_routes = routes.get(options)
        super(BlogServer, self).__init__(the_routes, **settings)
