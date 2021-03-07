# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class HrContract(models.Model):
    _inherit = 'hr.contract'

    descount_comedor = fields.Float(string="Descount comedor", default=0.00)
    descount_back_to_school = fields.Float(string="descount back to school", default=0.00)
    descount_glasses = fields.Float(string="Descount glasses", default=0.00)