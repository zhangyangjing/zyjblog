# -*- coding: utf-8 -*-

from tornado.web import StaticFileHandler


def get(options):
    return [
        (r'/static/(.*)', StaticFileHandler, {'path': options.static_dir}),

        # page
        ('/', 'controller.web.articles.ArticlesHandler'),
        ('/about', 'controller.web.about.AboutHandler'),
        ('/login', 'controller.web.user.LoginHandler'),
        ('/logout', 'controller.web.user.LogoutHandler'),
        ('/images', 'controller.web.images.ImagesHandler'),
        ('/images/(.*)', 'controller.web.images.ImagesHandler'),
        ('/articles', 'controller.web.articles.ArticlesHandler'),
        ('/articles/new', 'controller.web.edit.EditHandler'),
        ('/articles/create', 'controller.web.edit.EditHandler'),
        ('/articles/([0-9a-z]*)', 'controller.web.articles.ArticlesHandler'),
        ('/articles/([0-9a-z]*)/edit', 'controller.web.edit.EditHandler'),

        # service

        # ajax
        ('/api/articles', 'controller.ajax.articles.ArticlesHandler'),
        ('/api/articles/(.*)', 'controller.ajax.articles.ArticlesHandler'),
    ]
