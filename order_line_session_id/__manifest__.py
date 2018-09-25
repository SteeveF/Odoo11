# -*- coding: utf-8 -*-
{
    'name': "Order Line Session Id",

    'summary': """
        Adds a session id in the lines of Order Lines
        """,

    'description': """
        This Module Adds session id to order Lines in Sales orders and in Purchase orders
    """,

    'author': "alc media",
    'website': "https://www.alcmedia.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.12',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/templates.xml',
    ],

}
