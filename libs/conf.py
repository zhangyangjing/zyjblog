# -*- coding: utf-8 -*-

import os

from tornado.options import define


def define_app_options():
    define('debug', default=True)
    define('cookie_secret', default='<bad secret>')

    define('mongodb_host', default="127.0.0.1")
    define('db_name', default="zyjblog")

    define('port', default=8088)

    define('log_dir', default='/var/log/zyjblog')
    define('log_level', default=5)

    define('admin_user', default='zyj')
    define('admin_pswd', default=('3c9909afec25354d551dae21590bb26e38d53f217'
                                  '3b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba61'
                                  '3b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5'
                                  'c44c2'))

    define('static_dir', default=os.path.join(os.getcwd(), 'static'))
