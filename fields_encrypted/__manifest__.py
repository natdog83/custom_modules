# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Encrypted Fields Module For Odoo',
    'version': '10.0.0',
    'category': 'Security',
    'author': "LasLabs",
    'license': 'AGPL-3',
    'data' : ['view/partner.xml'],
    'depends': ['base'],
    "external_dependencies": {
        "python": [
            "Crypto",
        ],
    },
    'installable': True,
    'auto_install': True,
}
