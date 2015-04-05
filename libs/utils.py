# -*- coding: utf-8 -*-

import os
import conf
import logging
from tornado.options import options, parse_config_file, parse_command_line


def load_config():
    conf.define_app_options()
    parse_command_line(final=False)
    conf_filename = 'debug.conf'
    if not options.debug:
        conf_filename = "release.conf"
    if os.path.exists(conf_filename):
        parse_config_file(conf_filename, final=False)
    else:
        print '\x1b[0;31;40mERROR:\x1b[0m config file not exists'
        return False
    parse_command_line(final=True)
    return True


def setup_log(options):
    LEVELS = {
        1: logging.CRITICAL,
        2: logging.ERROR,
        3: logging.WARNING,
        4: logging.INFO,
        5: logging.DEBUG,  # 数字最大记录最详细
    }
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(threadName)s %(filename)s %(funcName)s \
                %(message)s')
    try:
        if not os.path.exists(options.log_dir):
            os.makedirs(options.log_dir)
        fileHandler = logging.handlers.RotatingFileHandler(
            options.log_dir + os.sep + "log.txt",
            maxBytes=1024 * 1024 * 10,
            backupCount=300)
    except IOError, e:
        print e
        return False
    else:
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(LEVELS.get(options.log_level))
        logging.getLogger('Main').addHandler(fileHandler)
        return True
