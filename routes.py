# -*- coding: utf-8 -*-

from tornado.web import StaticFileHandler


def get(options):
    return [
        (r'/static/(.*)', StaticFileHandler, {'path': options.static_dir}),


        ('/', 'controller.articles.ArticlesHandler'),
        ('/articles', 'controller.articles.ArticlesHandler'),
        ('/articles/([0-9a-z]*)', 'controller.articles.ArticlesHandler'),

        ('/about', 'controller.about.AboutHandler'),
        ('/profile', 'controller.profile.ProfileHandler'),
        ('/profile.pdf', 'controller.profile.ProfileHandler'),
        ('/login', 'controller.user.LoginHandler'),
        ('/logout', 'controller.user.LogoutHandler'),

        ('/images', 'controller.images.ImagesHandler'),
        ('/images/(.*)', 'controller.images.ImagesHandler'),
    ]
