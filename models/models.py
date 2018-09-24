# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sale_order_line_number(models.Model):

	_inherit='sale.order.line'
	line_sid = fields.Char('Serial Number')


class purchase_order_line_number(models.Model):

	_inherit='purchase.order.line'
	line_sid = fields.Char('Serial Number')


# class c:\users\steev\desktop\migration(models.Model):
#     _name = 'c:\users\steev\desktop\migration.c:\users\steev\desktop\migration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
