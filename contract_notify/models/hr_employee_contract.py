# -*- coding: utf-8 -*-
import datetime
from datetime import date
from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def sync_contract(self):
        message = []
        name = []
        obj_emp_contract = self.env['hr.employee.contract']
        obj_contract = self.env['hr.contract']
        contract = obj_contract.search([])
        emp_contract = obj_emp_contract.search([])
        
        if contract:
            for x in contract:
                d2 = datetime.datetime.utcnow().date()
                date_end = x.date_end or d2
                d1 = datetime.datetime.strptime(str(date_end), '%Y-%m-%d').date()
                r = d1 - d2
        
                if x.date_end:
                    if r.days <= 31 and r.days >= 0:
                        name.append(str(x.employee_id.name))
                        print name, "name#################"
                        self.write({'akan_habis': True})
                        if emp_contract:
                            for emp in emp_contract:
                                if emp.employee_id.id != x.employee_id.id:
                                    obj_emp_contract.create({
                                                                'employee_id': x.employee_id.id,
                                                                'date_start': x.date_start,
                                                                'date_end': x.date_end,
                                                                'contract_id': x.id,
                                                                'state': 'new'
                                                        })
                        else:
                            obj_emp_contract.create({
                                                        'employee_id': x.employee_id.id,
                                                        'date_start': x.date_start,
                                                        'date_end': x.date_end,
                                                        'contract_id': x.id,
                                                        'state': 'new'
                                                })

        if emp_contract:
            for emp in emp_contract:
                if emp.reads == True:
                    name.remove(str(emp.employee_id.name))

        message.append(name)
        if len(name) != 0:
            last = " akan segera Habis Kontrak. Check selengkapnya pada Menu Employee > End Contracts"
            message.append(last)
            self.env.user.notify_warning(message)

class HrEmployeeContract(models.Model):
    _name = 'hr.employee.contract'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _description = 'HR Employee (End Contract)'

    employee_id = fields.Many2one('hr.employee', 'Employee', readonly=True, required=True)
    date_start = fields.Char('Tanggal Mulai', readonly=True)
    date_end = fields.Char('Tanggal Akhir', readonly=True)
    reads = fields.Boolean('Sudah dibaca ?')
    contract_id = fields.Many2one('hr.contract', 'Contract')
    state = fields.Selection([('new', 'New'), ('done', 'Done'), ], string='Status')

    @api.multi
    def name_get(self):
        result = []
        for this in self:
            result.append((this.id, "[%s Habis Kontrak - %s]" % (this.employee_id.name.title(), this.date_end)))
        return result

    def read_this(self):
        self.write({'reads': True, 'state': 'done'})
        return True

    @api.model
    def _needaction_domain_get(self):
        return [('state', '=', 'new')]
