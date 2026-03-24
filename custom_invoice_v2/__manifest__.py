# -*- coding: utf-8 -*-
{
    'name': "custom_invoice_v2",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base',
                'account',
                'hr',
                #'employee_salespesrson',
                'l10n_gcc_invoice',
                'l10n_sa',
                'account_reports',
                'l10n_sa_edi',
                ],

    'data': [
        'views/views.xml',
        'views/custom_invoice_report.xml',
        'views/custom_invoice_no_header.xml',
        'views/account_move.xml',
    ],
}
