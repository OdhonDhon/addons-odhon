# -*- coding: utf-8 -*-
from odoo import http

# class AbHrRecruitment(http.Controller):
#     @http.route('/ab_hr_recruitment/ab_hr_recruitment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ab_hr_recruitment/ab_hr_recruitment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ab_hr_recruitment.listing', {
#             'root': '/ab_hr_recruitment/ab_hr_recruitment',
#             'objects': http.request.env['ab_hr_recruitment.ab_hr_recruitment'].search([]),
#         })

#     @http.route('/ab_hr_recruitment/ab_hr_recruitment/objects/<model("ab_hr_recruitment.ab_hr_recruitment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ab_hr_recruitment.object', {
#             'object': obj
#         })