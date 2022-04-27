from odoo import api, fields, models

class ResUser(models.Model):
    _name = 'res_user'
    _inherit = 'res_user'

    old_id = fields.Char(string='Old ID', readonly=True)