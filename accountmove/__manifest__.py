# -*- coding: utf-8 -*-
{
    'name': 'Invoicing',
    'version': '1.1',
    'summary': """
       This is a sub module for Accounting invoice""",

    'description': """
        This is an Hospital Management application which is developed for manage all hospital needs.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing',


    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/acoount_move_inherit.xml'
    ],
    'installable': True
}
