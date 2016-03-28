#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import hashlib
from tornado.web import HTTPError
from tornado.options import options
from libs.handler import BaseHandler


class ImagesHandler(BaseHandler):
    def get(self, image_name):
        file_path = '%s/%s/%s/%s' % (options.images_dir,
                                     image_name[0:2],
                                     image_name[2:4],
                                     image_name)
        if not os.path.exists(file_path):
            raise HTTPError(404)
        with open(file_path) as f:
            self.finish(f.read())

    def post(self):
        data = []
        for file_info in self.request.files['file']:
            file_path = self._get_file_path(file_info)
            dir_path = os.path.dirname(file_path)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            with open(file_path, 'w+') as f:
                f.write(file_info['body'])
            data.append(os.path.basename(file_path))
        self.finish({'images': data})

    def _get_file_path(self, file_info):
        file_name = self._get_file_hash_name(file_info)
        return '%s/%s/%s/%s' % (options.images_dir,
                                file_name[0:2],
                                file_name[2:4],
                                file_name)

    def _get_file_hash_name(self, file_info):
        file_hash = hashlib.md5(file_info['body']).hexdigest()
        extension = file_info['content_type'].split('/')[1]
        extension = ('jpeg' == extension and ['jpg'] or [extension])[0]
        return '%s.%s' % (file_hash, extension)
