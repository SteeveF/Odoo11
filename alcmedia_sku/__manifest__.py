# -*- coding: utf-8 -*-
{
    'name': "alcmedia_sku",

    'summary': """
        Make internal product reference unique for all Products""",

    'description': """
        Make internal product reference unique for all Products
    """,

    'author': "alc media",
    'website': "http://www.alcmedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'views/templates.xml',
    ],

}
