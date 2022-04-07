from odoo import api, fields, models, _
from home.hp.odoo.custom.crypt.fields_encrypted.fields import EncryptedText

class Partner(models.Model):
    _inherit = 'res.partner'

    mobile_crypt = fields.Char(string='Encrypted Mobile')

    @api.onchange('mobile')
    def onchange_mobile(self):
        for rec in self:
            print ("----record---------",rec)
            # res = EncryptedText._new_field()._encrypt(rec.mobile)
            # print ("----Res----",res)
            # rec.mobile_crypt = res