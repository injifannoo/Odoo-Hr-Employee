from odoo import models, fields, api

class HREmployee(models.Model):
    _name = 'hr_system.employee'
    _description = 'Employee Record'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    department_id = fields.Many2one('hr_system.department', string="Department")
    retirement_age = fields.Integer(string='Retirement Age', compute='_compute_retirement_age')

    @api.depends('age')
    def _compute_retirement_age(self):
        for rec in self:
            rec.retirement_age = 65 - rec.age if rec.age else 0

