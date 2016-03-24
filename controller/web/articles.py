# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from tornado.options import options
from libs.handler import BaseHandler


class ArticlesHandler(BaseHandler):
    def get(self, article_id=None):
        if article_id is None:
            self._get_all()
        else:
            self._get_special(article_id)

    def _get_special(self, article_id):
        article = self.db.articles.find_one({'_id': ObjectId(article_id)},
                                            {'data': 1, 'title': 1})
        self.render('article.html',
                    title=article['title'],
                    article=self.md.convert(article['data']))

    def _get_all(self):
        articles = self.db.articles.find({}, {'_id': 1, 'title': 1})
        self.render('articles.html',
                    articles=articles,
                    admin=options.admin_user == self.current_user)
