# -*- coding: utf-8 -*-
# Copyright 2016 Eficent Business and IT Consulting Services S.L.
# (http://www.eficent.com)
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def do_print_checks(self):
        for rec in self:
            if rec.company_id.check_layout_id:
                return self.env['report'].get_action(
                    rec, rec.company_id.check_layout_id.report)
            return super(AccountPayment, self).do_print_checks()
