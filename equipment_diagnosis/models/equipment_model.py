# -*- coding: utf-8 -*-

from odoo import fields, models


class EquipmentModel(models.Model):
    _name = "equipment.model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Equipment Model"

    name = fields.Char(string="Model Name", required=True)
    company_id = fields.Many2one(
        "res.company", string="Company", default=lambda self: self.env.company
    )
    category_id = fields.Many2one("equipment.category", string="Category")
    note = fields.Html("Note")
    supplier_id = fields.Many2one("res.partner", string="Vendor")
    supplier_ref = fields.Char("Vendor Reference")
    color = fields.Integer("Color Index")
