# -*- coding: utf-8 -*-

from tornado.web import StaticFileHandler


def get(options):
    return [
        (r'/static/(.*)', StaticFileHandler, {'path': options.static_dir}),

        # page
        ('/', 'controller.web.index.IndexHandler'),

        # service

        # ajax
        ('/api/articles', 'controller.ajax.article.ArticleHandler'),
        ('/api/articles/(.*)', 'controller.ajax.article.ArticleHandler'),
    ]
