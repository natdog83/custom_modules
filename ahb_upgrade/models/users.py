from odoo import api, fields, models

class ResUser(models.Model):
    _name = 'res.user'
    _inherit = 'res.user'

    old_id = fields.Char(string='Old ID', readonly=True)