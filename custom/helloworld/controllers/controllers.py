from odoo import http

class HelloWorldController(http.Controller):

    @http.route('/helloworld', type='http', auth='public', website=True)
    def hello_world(self, **kw):
        return "<h1>Hello World</h1>"
