# -*- coding: utf-8 -*-

from odoo import fields, models


class Survey(models.Model):
    _inherit = "survey.survey"

    equipment_model_id = fields.Many2one("equipment.model", string="Equipment")
