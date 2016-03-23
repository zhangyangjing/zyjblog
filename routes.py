# -*- coding: utf-8 -*-

from tornado.web import StaticFileHandler


def get(options):
    return [
        (r'/static/(.*)', StaticFileHandler, {'path': options.static_dir}),

        # page
        ('/', 'controller.web.articles.ArticlesHandler'),
        ('/articles', 'controller.web.articles.ArticlesHandler'),
        ('/articles/([0-9a-z]*)', 'controller.web.articles.ArticlesHandler'),

        # service

        # ajax
        ('/api/articles', 'controller.ajax.articles.ArticlesHandler'),
        ('/api/articles/(.*)', 'controller.ajax.articles.ArticlesHandler'),
    ]
