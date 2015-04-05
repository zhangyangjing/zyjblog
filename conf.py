# -*- coding: utf-8 -*-

from tornado.options import define


def define_app_options():
    define('debug', default=True)
    define('cookie_secret', default='<bad secret>')

    define('mongodb_host', default="127.0.0.1")
    define('db_name', default="zyjblog")

    define('port', default=8088)

    define('log_dir', default='/var/log/zyjblog')
    define('log_level', default=5)
