#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from datetime import datetime
from bson.objectid import ObjectId


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def bson_2_json(data):
    return json.loads(MyEncoder().encode(data))
