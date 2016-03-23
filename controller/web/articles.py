# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from libs.handler import BaseHandler


class ArticlesHandler(BaseHandler):
    def get(self, article_id=None):
        if article_id is None:
            self._get_all()
        else:
            self._get_special(article_id)

    def _get_special(self, article_id):
        object_id = ObjectId(article_id)
        d = self.db.articles.find_one({'_id': object_id}, {'data': 1})
        html = self.md.convert(d['data'])
        self.render('article.html', article=html)

    def _get_all(self):
        d = self.db.articles.find({}, {'_id': 1, 'title': 1})
        self.render('articles.html', articles=d)
