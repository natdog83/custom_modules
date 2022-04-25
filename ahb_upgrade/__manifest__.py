# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'AHB Upgrade',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'This modules addes fields to the account and product modules to link them to the v9',
    'description': """

    """,
    'depends': [],
    'data': [
        'views/partner_view.xml'
    ],
    'installable': True,
    'auto_install': False,
#    'post_init_hook': 'create_check_sequence_on_bank_journals',
    'license': 'LGPL-3',
}