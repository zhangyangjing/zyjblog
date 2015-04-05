#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.httpserver import HTTPServer

from libs.server import BlogServer
from libs.utils import load_config, setup_log


def main():
    if False == load_config():
        return -1
    if False == setup_log(options):
        return -1

    log = logging.getLogger('Main.server')
    logging.info("Starting at port %s in %s mode",
                 options.port,
                 'debug' if options.debug else 'release')

    app = BlogServer(options)
    server = HTTPServer(app, xheaders=True)
    server.listen(options.port)
    log.info('Everything seems good. Ready to Roll!')
    IOLoop.instance().start()
    log.info('Exiting...waiting for background jobs done...')
    app.db.connection.close()
    log.info('Done. Bye.')


if __name__ == '__main__':
    sys.exit(main())
