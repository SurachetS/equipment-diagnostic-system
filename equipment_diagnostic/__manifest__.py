# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Equipment Diagnostic",
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
        "views/diagnostic_menu.xml",
        "views/equipment_category_views.xml",
        "views/equipment_views.xml",
        "views/survey_question_views.xml",
        "views/survey_survey_views.xml",
        "views/survey_templates_management.xml",
        "views/survey_templates_print.xml",
        "views/survey_templates.xml",
        "views/diagnostic_selector_templates.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "maintainers": ["SurachetS"],
    "license": "OPL-1",
}
