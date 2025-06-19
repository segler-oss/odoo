# -*- coding: utf-8 -*-
from odoo import http


class Goodbye(http.Controller):
    @http.route('/goodbye', auth='public')
    def index(self, **kw):
        return "Hello, world"
