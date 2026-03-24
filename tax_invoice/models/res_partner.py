# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import  UserError
import math


class AccountMove(models.Model):
    _inherit = 'res.partner'


    additional_no = fields.Char()
    cr_no = fields.Char(string="CR No.")
    arabic_name = fields.Char('Arabic Name', size=120)
    arabic_city = fields.Char('Arabic City', size=120)
    arabic_street = fields.Char('Arabic Street', size=120)
    arabic_street2 = fields.Char('Arabic Street2', size=120)

    custom_invoice = fields.Boolean()


