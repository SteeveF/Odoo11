# -*- coding: utf-8 -*-
from odoo import models, fields, api

class unique_sku(osv.osv):
    _inherit = 'product.template'

    _sql_constraints = [
        ('unique_sku', 'unique(default_code)', 'This internal reference already exists.'),
    ]

unique_sku()
