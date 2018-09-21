# -*- coding: utf-8 -*-
from odoo import http

# class C:\users\steev\desktop\migration\modules\odoo11\orderLinesSid(http.Controller):
#     @http.route('/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid.listing', {
#             'root': '/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid',
#             'objects': http.request.env['c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid.c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid'].search([]),
#         })

#     @http.route('/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid/objects/<model("c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid.c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('c:\users\steev\desktop\migration\modules\odoo11\order_lines__sid.object', {
#             'object': obj
#         })