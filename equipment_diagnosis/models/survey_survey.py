# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.osv import expression


class Survey(models.Model):
    _inherit = "survey.survey"

    equipment_id = fields.Many2one("maintenance.equipment", string="Equipment")
    questions_selection = fields.Selection(
        selection_add=[("decision_tree", "Decision Tree")],
        ondelete={"decision_tree": "cascade"},
    )


    def _get_next_page_or_question(self, user_input, page_or_question_id, go_back=False):
        # XXX - START

        if self.questions_selection == 'decision_tree':
            survey = user_input.survey_id
            pages_or_questions = survey._get_pages_or_questions(user_input)
            current_question = self.env['survey.question'].browse(page_or_question_id)
            Question = self.env['survey.question']

            print("DEBUG: User Input Lines")
            for user_input_line_id in user_input.user_input_line_ids:
                print(user_input_line_id)
            print("DEBUG END")

            # Handle Next Question
            if not go_back:
                if not pages_or_questions:
                    return Question

                # First page or question
                if page_or_question_id == 0:
                    return pages_or_questions[0]
            else:
                # Handle Previous Question
                if current_question:
                    # Find the most recent user input line with a next_question_id matching the current question
                    user_input_line = user_input.user_input_line_ids.filtered(
                        lambda line: line.suggested_answer_id.next_question_id == current_question
                    )
                    if len(user_input_line) > 1:
                        user_input_line = user_input_line[-1]

                    if user_input_line:
                        prev_question = user_input_line.question_id
                        return prev_question

            # Handle edge cases
            if not page_or_question_id:
                return page_or_question_id

            current_page_index = pages_or_questions.ids.index(page_or_question_id)

            # Check if on the first or last page/question
            if (go_back and current_page_index == 0) or (not go_back and current_page_index == len(pages_or_questions) - 1):
                return Question

            # Find the user input line for the current question
            if current_question:
                user_input_line = user_input.user_input_line_ids.filtered(
                    lambda line: line.question_id == current_question
                )

                if user_input_line:
                    if len(user_input_line) > 1:
                        user_input_line = user_input_line[-1]

                    selected_answer = user_input_line.suggested_answer_id
                    next_question = selected_answer.next_question_id

                    if next_question:
                        print("DEBUG: Next Question")
                        print(f"Selected Answer: {selected_answer}")
                        print(f"Next Question: {next_question.title}")
                        print(f"Current Question: {current_question.title}")
                        print(f"User Input Line Question: {user_input_line.question_id.title}")
                        print("DEBUG END")
                        return next_question

            # Return empty question if no next question is found
            return self.env['survey.question']

        # XXX - END

        else:
            return super()._get_next_page_or_question(user_input=user_input, page_or_question_id=page_or_question_id, go_back=go_back)

    def _get_survey_questions(self, answer=None, page_id=None, question_id=None):
        if self.questions_selection == 'decision_tree':
            if answer and answer.is_session_answer:
                return self.session_question_id, self.session_question_id.id
            if self.questions_layout == 'page_per_section':
                if not page_id:
                    raise ValueError("Page id is needed for question layout 'page_per_section'")
                page_or_question_id = int(page_id)
                questions = self.env['survey.question'].sudo().search(
                    expression.AND([[('survey_id', '=', self.id)], [('page_id', '=', page_or_question_id)]]))
            elif self.questions_layout == 'page_per_question':
                if not question_id:
                    raise ValueError("Question id is needed for question layout 'page_per_question'")
                page_or_question_id = int(question_id)
                questions = self.env['survey.question'].sudo().browse(page_or_question_id)
            else:
                page_or_question_id = None
                questions = self.question_ids

            return questions, page_or_question_id

        return super()._get_survey_questions(answer=answer, page_id=page_id, question_id=question_id)

