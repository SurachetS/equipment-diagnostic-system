# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Equipment Diagnosis",
    "version": "18.0.1.0.0",
    "category": "Maintenance",
    "summary": "",
    "description": """
    """,
    "website": "http://prothaitechnology.com",
    "author": "Surachet Saejueng",
    "depends": [
        "mail",
        "maintenance",
        "survey",
    ],
    "data": [
        "views/base_views.xml",
        "views/diagnosis_menu.xml",
        "views/equipment_category_views.xml",
        "views/equipment_views.xml",
        "views/survey_question_views.xml",
        "views/survey_survey_views.xml",
        "views/survey_templates_management.xml",
        "views/survey_templates_print.xml",
        "views/survey_templates.xml",
        "views/diagnosis_selector_templates.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "maintainers": ["SurachetS"],
    "license": "OPL-1",
}
