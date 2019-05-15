# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    @api.one
    @api.constrains('email_from')
    def check_email(self):
        email = self.email_from
        obj_applicant = self.env['hr.applicant']
        data_applicant = obj_applicant.search([('email_from', '=', email)])
        data = 0
        for x in data_applicant:
            data = data + 1
            if data > 1:
                raise ValidationError("Error Occured !")