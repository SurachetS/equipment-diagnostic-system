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
        "survey",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/base_views.xml",
        "views/equipment_category_views.xml",
        "views/equipment_model_views.xml",
        "views/survey_survey_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "maintainers": ["SurachetS"],
    "license": "OPL-1",
}
