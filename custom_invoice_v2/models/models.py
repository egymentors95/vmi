# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_discount = fields.Monetary(string='Discount Amount', compute='_compute_amount_discount')
    project_name = fields.Char('Project Name')
    project_po_number = fields.Char('PO Number')

    prepared_by = fields.Many2one(
        'hr.employee',  # Related model
        string='Prepared By',  # Field label
        default=lambda self: self.env['hr.employee'].search([('user_id', '=', self.env.user.id)], limit=1).id,
    )


    total_discount = fields.Float(string="Total Discount", compute='_compute_total_discount', store=True)
    total_before_discount = fields.Float(string="Total Before Discount", compute='_compute_total_before_discount', store=True)

    @api.depends('invoice_line_ids.discount', 'invoice_line_ids.price_subtotal')
    def _compute_total_discount(self):
        for move in self:
            total_discount = 0.0
            for line in move.invoice_line_ids:
                if line.discount:
                    total_discount += (line.price_unit * line.discount / 100) * line.quantity
            move.total_discount = total_discount

    @api.depends('invoice_line_ids.price_subtotal', 'total_discount')
    def _compute_total_before_discount(self):
        for move in self:
            total_before_discount = sum(line.price_unit * line.quantity for line in move.invoice_line_ids)
            move.total_before_discount = total_before_discount

    @api.depends('invoice_line_ids.price_discount')
    def _compute_amount_discount(self):
        for move in self:
            move.amount_discount = sum(move.invoice_line_ids.mapped('price_discount'))


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    employee_time_sheet = fields.Char("Duration of service")
    price_discount = fields.Monetary(string='Discount Amount', compute='_compute_price_discount')

    @api.depends('price_subtotal', 'price_unit', 'quantity')
    def _compute_price_discount(self):
        for line in self:
            line.price_discount = round(line.price_unit * line.quantity - line.price_subtotal, 2)


class ExtendRes(models.Model):
    _inherit = 'res.partner'

    customer_cr_number = fields.Char('Customer CR')