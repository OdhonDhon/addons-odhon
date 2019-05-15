# -*- coding: utf-8 -*-
{
    'name': "Image On Xls",
    'summary': """
        simple module, example Image on xls (XLWT).
    """,
    'description': """
        this module is an example how to put an image to xls (XLWT).
    """,
    'author': "Dani Ramdani",
    'website': "http://ismata.co.id",
    'category': 'Example',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/xlwt_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
