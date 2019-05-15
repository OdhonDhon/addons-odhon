# -*- coding: utf-8 -*-
{
    'name': " HR Recruitment Validation",
    'summary': """ Customized HR Recruitment """,
    'description': """
        This module's purpose is to customized HR Recruitment.
    """,
    'author': "Dani Ramdani",
    'website': "https://ismata.co.id",
    'category': 'HR',
    'version': '0.1',
    'depends': ['base', 'hr_recruitment', 'website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}