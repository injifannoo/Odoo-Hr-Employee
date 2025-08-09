from odoo import models, fields

class HREmployee(models.Model):
    _name = 'hr.employee'
    _description = 'Employee Record'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    department = fields.Char(string='Department')
    department_id = fields.Many2one('hr.department', string="Department")
