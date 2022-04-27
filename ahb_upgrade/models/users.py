from odoo import api, fields, models

class ResUsers(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    old_id = fields.Char(string='Old ID', readonly=True)