#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import markdown2


class Markdown(markdown2.Markdown):

    _re_h1_title = re.compile('<h1>(.*)</h1>')

    def postprocess(self, text):
        r = self._re_h1_title.search(text)
        self.title = (r is None and [None] or [r.group(1)])[0]
        return text
