# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Brewery Management Application',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'This application is to turn Odoo into a brewery management software',
    'description': """
This application adds fundtionality to the manufacturing module to 
track batches of beer, to track turns of the brewhouse and to track analytics 
of the entire process. 
    """,
    'depends': [],
    'data': [

    ],
    'installable': True,
    'auto_install': False,
#    'post_init_hook': 'create_check_sequence_on_bank_journals',
    'license': 'LGPL-3',
}