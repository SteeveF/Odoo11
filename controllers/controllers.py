# -*- coding: utf-8 -*-
from odoo import http

class C:\users\steev\desktop\migration(http.Controller):
    @http.route('/c:\users\steev\desktop\migration/c:\users\steev\desktop\migration/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/c:\users\steev\desktop\migration/c:\users\steev\desktop\migration/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('c:\users\steev\desktop\migration.listing', {
            'root': '/c:\users\steev\desktop\migration/c:\users\steev\desktop\migration',
            'objects': http.request.env['c:\users\steev\desktop\migration.c:\users\steev\desktop\migration'].search([]),
        })

    @http.route('/c:\users\steev\desktop\migration/c:\users\steev\desktop\migration/objects/<model("c:\users\steev\desktop\migration.c:\users\steev\desktop\migration"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('c:\users\steev\desktop\migration.object', {
            'object': obj
        })