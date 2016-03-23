# -*- coding: utf-8 -*-

'''
    {
        _id: sk3kj2kj4,
        data: "sdfdsf",
        history: [
            {
                data: "df",
                time: time,
                ip: "123,34,234,3"
            }
        ]
    }
'''

from datetime import datetime
from bson.objectid import ObjectId
from libs.handler import BaseHandler


class ArticleHandler(BaseHandler):
    def get(self):
        self.finish('article get')

    def post(self):
        data = {'history': []}
        self._update_data(data, self.get_argument('markdown'))
        article_id = self.db.articles.save(data)
        self.set_status(201)
        self.write({'article_id': str(article_id)})

    def put(self, article_id):
        data = self.db.articles.find_one({'_id': ObjectId(article_id)})
        data['history'].append({
            'data': data['data'],
            'time': data['time'],
            'address': data['address']
        })
        self._update_data(data, self.get_argument('markdown'))
        self.db.articles.save(data)

    # data, time, title, tags, address
    def _update_data(self, data, article_data):
        data['data'] = article_data
        data['time'] = datetime.now()
        data['title'] = 'sdf'
        data['tags'] = []
        data['address'] = (self.request.headers.get("X-Real-IP") or
                           self.request.remote_ip)
