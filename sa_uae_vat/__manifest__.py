# -*- coding: utf-8 -*-
# Copyright (C) 2017-Today  Technaureus Info Solutions(<http://technaureus.com/>).

{
    'name': 'Saudi/UAE VAT(Arabic VAT)',
    'version': '18.0.0.1',  # Updated version for Odoo 18
    'sequence': 1,
    'category': 'Localization',
    'summary': 'SA UAE VAT configuration',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'price': 20,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'description': """
This module is for configure of Saudi and UAE VAT
    """,
    'depends': ['account', 'product'],
    'data': [
        'views/product_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml'
    ],
    'images': ['images/main_screenshot.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}