# -*- coding: utf-8 -*-

from ast import literal_eval
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class MaintenanceEquipmentCategory(models.Model):
    _inherit = ["maintenance.equipment.category"]

    active = fields.Boolean(default=True)
