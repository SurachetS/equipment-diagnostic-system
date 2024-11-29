# -*- coding: utf-8 -*-

from ast import literal_eval
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class EquipmentCategory(models.Model):
    _name = "equipment.category"
    _inherit = ["mail.thread", "avatar.mixin"]
    _description = "Equipment Category"
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = "complete_name"
    _order = "complete_name"

    name = fields.Char("Category Name", required=True)
    complete_name = fields.Char(
        "Complete Name", compute="_compute_complete_name", recursive=True, store=True
    )
    parent_id = fields.Many2one(
        "equipment.category", string="Parent Category", index=True, ondelete="restrict"
    )
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(
        "equipment.category", "parent_id", string="Child Categories"
    )
    color = fields.Integer("Color Index")
    note = fields.Html("Comments", translate=True)
    equipment_model_ids = fields.One2many(
        "equipment.model", "category_id", string="Equipment Models", copy=False
    )
    equipment_model_count = fields.Integer(
        string="Equipment Model Count", compute="_compute_equipment_model_count"
    )

    @api.depends("name", "parent_id.complete_name")
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = "%s / %s" % (
                    category.parent_id.complete_name,
                    category.name,
                )
            else:
                category.complete_name = category.name

    @api.constrains("parent_id")
    def _check_category_recursion(self):
        if self._has_cycle():
            raise ValidationError(_("You cannot create recursive categories."))

    @api.model
    def name_create(self, name):
        category = self.create({"name": name})
        return category.id, category.display_name

    @api.depends_context("hierarchical_naming")
    def _compute_display_name(self):
        if self.env.context.get("hierarchical_naming", True):
            return super()._compute_display_name()
        for record in self:
            record.display_name = record.name

    @api.depends("equipment_model_ids")
    def _compute_equipment_model_count(self):
        for obj in self:
            obj.equipment_model_count = len(obj.equipment_model_ids)

    def action_view_equipment_model_ids(self):
        self.ensure_one()
        res_ids = self.equipment_model_ids.ids
        action = self.env.ref("equipment_diagnosis.action_equipment_model").read()[0]
        action["domain"] = [("id", "in", res_ids)]
        context = action.get("context", {})
        if isinstance(context, str):
            context = literal_eval(context)
        context["create"] = False
        context["default_domain"] = [("id", "in", res_ids)]
        context["expand"] = 1
        action["context"] = context
        return action
