# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json


class DiagnosticController(http.Controller):

    @http.route("/diagnostic/selector", type="http", auth="public")
    def diagnostic_selector(self):
        # ดึงข้อมูล Category
        categories = request.env["maintenance.equipment.category"].sudo().search([])
        return request.render("equipment_diagnosis.diagnostic_selector_page", {"categories": categories})

    @http.route("/diagnostic/equipments", type="http", auth="public")
    def get_equipments(self, category_id=None):
        if not category_id:
            # ส่งกลับข้อความผิดพลาดถ้าไม่มี category_id
            response = {"error": "Missing category_id"}
            return request.make_response(json.dumps(response), headers={"Content-Type": "application/json"}, status=400)
        try:
            category_id = int(category_id)  # แปลง category_id เป็นตัวเลข
        except ValueError:
            # ส่งกลับข้อความผิดพลาดถ้า category_id ไม่ใช่ตัวเลข
            response = {"error": "Invalid category_id"}
            return request.make_response(json.dumps(response), headers={"Content-Type": "application/json"}, status=400)

        # ดึงข้อมูล Equipment ตาม Category
        equipments = (request.env["maintenance.equipment"].sudo().search([("category_id", "=", category_id)]))
        result = [{"id": eq.id, "name": eq.name} for eq in equipments]
        return request.make_response(json.dumps(result), headers={"Content-Type": "application/json"})

    @http.route("/diagnostic/surveys", type="http", auth="public")
    def get_surveys(self, equipment_id=None):
        if not equipment_id:
            response = {"error": "Missing equipment_id"}
            return request.make_response(json.dumps(response), headers={"Content-Type": "application/json"}, status=400)
        try:
            equipment_id = int(equipment_id)
        except ValueError:
            response = {"error": "Invalid equipment_id"}
            return request.make_response(json.dumps(response), headers={"Content-Type": "application/json"}, status=400)

        # ดึงข้อมูล Survey ตาม Equipment
        surveys = (request.env["survey.survey"].sudo().search([("equipment_id", "=", equipment_id)]))
        result = [{"id": survey.id, "title": survey.title} for survey in surveys]
        return request.make_response(json.dumps(result), headers={"Content-Type": "application/json"})

    @http.route("/diagnostic/survey/start/<int:survey_id>", type="http", auth="public")
    def custom_survey_start(self, survey_id):
        # ค้นหา Survey ด้วย ID
        survey = request.env["survey.survey"].sudo().browse(survey_id)
        if not survey.exists():
            return request.not_found()

        # ดึง Access Token จาก Survey
        access_token = survey.access_token
        if not access_token:
            return request.not_found()

        # Redirect ไปยัง Controller หลักของ Survey
        return request.redirect(f"/survey/start/{access_token}")
