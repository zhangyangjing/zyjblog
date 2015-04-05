# -*- coding: utf-8 -*-

from tornado.web import UIModule


class ExamplePicker(UIModule):
    def render(self):
        return '''
            <label>uimodule test</label>
        '''

    def embedded_javascript(self):
        pass
