# -*- coding: utf-8 -*-

from jinja2 import Environment
from jinja2 import FileSystemLoader


class JinjaLoader(object):
    def __init__(self, root_path, **kwargs):
        super(JinjaLoader, self).__init__()
        auto_reload = kwargs.get('debug', True)
        self.env = Environment(loader=FileSystemLoader(root_path),
                               extensions=['jinja2.ext.autoescape'],
                               trim_blocks=True,
                               lstrip_blocks=True,
                               cache_size=-1,  # no clean-up
                               auto_reload=auto_reload)

        additional_globals = {
            'ord': ord,
            'chr': chr,
            'unichr': unichr,
        }
        self.env.globals.update(additional_globals)
        self.env.add_extension('jinja2.ext.loopcontrols')

    def load(self, name, parent_path=None):
        return JinjaTemplate(self.env.get_template(name))

    def reset(self):
        '''Reset the cache of compiled templates, required
           in debug mode.
        '''
        self.env.cache.clear()


class JinjaTemplate(object):
    def __init__(self, template):
        self.template = template

    def generate(self, **kwargs):
        # jinja uses unicode internally but tornado uses utf string
        return self.template.render(**kwargs).encode('utf-8')
