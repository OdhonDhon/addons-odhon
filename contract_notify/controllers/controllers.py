# -*- coding: utf-8 -*-
from odoo import http

# class ContractNotif(http.Controller):
#     @http.route('/contract_notif/contract_notif/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contract_notif/contract_notif/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contract_notif.listing', {
#             'root': '/contract_notif/contract_notif',
#             'objects': http.request.env['contract_notif.contract_notif'].search([]),
#         })

#     @http.route('/contract_notif/contract_notif/objects/<model("contract_notif.contract_notif"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contract_notif.object', {
#             'object': obj
#         })