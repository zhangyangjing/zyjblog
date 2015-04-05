# -*- coding: utf-8 -*-

import md5
import datetime


class User():
    def __init__(self, user_name):
        self.user_name = user_name


def create_user(handler, user_name, user_pswd):
    user = handler.db.users.find_one(user_name)
    if user is not None:
        return False

    data = {
        '_id': user_name,
        'pswd': _encrypt_user_pswd(user_name, user_pswd),
        'time': datetime.datetime.now()
    }
    handler.db.users.save(data)
    return True


def check_user(handler, user_name, user_pswd):
    user = handler.db.users.find_one({'_id': user_name}, ['pswd'])
    if user is None:
        return False

    encrypted_pswd = _encrypt_user_pswd(user_name, user_pswd)
    if encrypted_pswd == user['pswd']:
        return True
    else:
        return False


def get_user(handler, user_name):
    u = handler.db.users.find_one(user_name)
    if u is None:
        return None
    return User(u['_id'])


def _encrypt_user_pswd(username, password):
    return md5.new(username + '#zyj#' + password).hexdigest()
