from odoo import models, fields

class Department(models.Model):
    _name = 'hr_system.department'
    _description = 'Department'

    name = fields.Char(string="Department Name", required=True)
    manager_id = fields.Many2one('hr_system.employee', string="Manager")
    employee_ids = fields.One2many('hr_system.employee', 'department_id', string="Employees")