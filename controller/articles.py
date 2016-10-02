# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime
from bson.objectid import ObjectId
from tornado.options import options
from libs.handler import BaseHandler
from tornado.web import authenticated


class ArticlesHandler(BaseHandler):
    def get(self, article_id=None):
        if article_id is None:
            self._get_all()
        else:
            self._get_special(article_id)

    @authenticated
    def post(self, article_id=None):
        content = self.get_body_argument("content", default=None, strip=False)

        if article_id is None:
            # create new article
            data = self._generate_new_article()
            self.db.articles.save(data)
            print str(data['_id'])
            self.set_status(307)
            self.set_header("Location", '/articles/' + str(data['_id']))
            self.finish()
        elif content is None:
            # edit article
            self.render('edit.html', article_id=article_id)

    @authenticated
    def put(self, article_id):
        # update article
        data = self.db.articles.find_one({'_id': ObjectId(article_id)})
        if data['markdown'] == self.get_argument('markdown'):
            return

        data['history'].append({
            'markdown': data['markdown'],
            'time': data['time']
        })
        self._update_article_data(data, self.get_argument('markdown'))
        self.db.articles.save(data)

    @authenticated
    def delete(self, article_id):
        print 'delete'
        self.db.articles.remove({'_id': ObjectId(article_id)})

    def _get_special(self, article_id):
        article = self.db.articles.find_one({'_id': ObjectId(article_id)},
                                            {'markdown': 1, 'title': 1})
        self.render('article.html',
                    title=article['title'],
                    article=self.md.convert(article['markdown']))

    def _get_all(self):
        articles = self.db.articles.find({}, {'_id': 1, 'title': 1})
        articles.sort('_id', pymongo.DESCENDING)
        self.render('articles.html',
                    articles=articles,
                    admin=options.admin_user == self.current_user)

    def _generate_new_article(self):
        data = {}
        data['markdown'] = ''
        data['time'] = datetime.now()
        data['title'] = None
        data['tags'] = []
        data['history'] = []
        return data

    def _update_article_data(self, data, markdown):
        self.md.convert(markdown)
        data['markdown'] = markdown
        data['time'] = datetime.now()
        data['title'] = self.md.title
        data['tags'] = []
