# -*- coding: utf-8 -*-

from datetime import datetime
from bson.objectid import ObjectId
from libs.handler import BaseHandler
from libs.json_helper import bson_2_json


class ArticlesHandler(BaseHandler):
    def get(self, article_id=None):
        if article_id is None:
            self._get_all()
        else:
            self._get_special(article_id)

    def post(self):
        data = {'history': []}
        self._update_data(data, self.get_argument('markdown'))
        self.set_status(201)
        del data['history']
        self.finish(bson_2_json(data))

    def put(self, article_id):
        data = self.db.articles.find_one({'_id': ObjectId(article_id)})
        data['history'].append({
            'data': data['data'],
            'time': data['time'],
            'address': data['address']
        })
        self._update_data(data, self.get_argument('markdown'))
        self.db.articles.save(data)
        del data['history']
        self.finish(bson_2_json(data))

    # data, time, title, tags, address
    def _update_data(self, data, article_data):
        self.md.convert(article_data)
        data['data'] = article_data
        data['time'] = datetime.now()
        data['title'] = self.md.title
        data['tags'] = []
        data['address'] = (self.request.headers.get("X-Real-IP") or
                           self.request.remote_ip)

    def _get_special(self, article_id):
        article = self.db.articles.find_one({'_id': ObjectId(article_id)},
                                            {'history': 0})
        self.finish(bson_2_json(article))

    def _get_all(self):
        articles = self.db.articles.find({}, {'history': 0})
        self.finish(bson_2_json(articles))
