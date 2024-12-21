# -*- coding: utf-8 -*-

from odoo import fields, models


class SurveyQuestionAnswer(models.Model):
    _inherit = "survey.question.answer"

    next_question_id = fields.Many2one(
        "survey.question",
        string="Next Question",
        domain="""[
            ('survey_id', '=', parent.survey_id),
            ('is_page', '=', False),
        ]""",
        help="The question to display after selecting this answer.",
    )
