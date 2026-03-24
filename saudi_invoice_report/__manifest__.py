# -*- coding: utf-8 -*-
{
    'name': "Saudi Invoice Report",

    'summary': """
        Saudi Invoice Report""",

    'description': """
        Saudi Invoice Report
    """,

    'author': "erp-bank",
    'website': "www.erp-bank.com",

    'category': 'Uncategorized',
    'version': '18.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','account_accountant','web','sa_uae_vat','l10n_sa'],

    # always loaded
    'data': [
        'views/res_company_view.xml',
        'views/vat_invoice_view.xml',
        'reports/saudi_report_layout.xml',
        'reports/saudi_invoice_report.xml',
        'data/mail_template_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
