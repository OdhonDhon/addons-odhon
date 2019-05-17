# -*- coding: utf-8 -*-
{
    'name': "Contract Notification",
    'summary': """
        HR Contract Notification
    """,
    'description': """
        With this module, we could get Notification 
        about Employees that their contracts will be End soon
    """,
    'author': "Dani Ramdani",
    'website': "https://www.ismata.co.id",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'hr_contract', 'web_notify'],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}