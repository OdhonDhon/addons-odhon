# -*- coding: utf-8 -*-
{
    'name': "Zoom Image - HR Employee",
    'summary': """
        To Zoom Image so clearly to see the Image.
    """,
    'description': """
        With this module, we could zoom an Employee Image when mouse hovering on it.
    """,
    'author': "Dani Ramdani",
    'website': "https://ismata.co.id",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'hr'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        # 'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}