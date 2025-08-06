from odoo import models, fields

class Employee(models.Model):
    _name = 'x_hr.employee'
    _description = 'Employee'

    name = fields.Char(string='Full Name', required=True)
    job_title = fields.Char(string='Job Title')
    department = fields.Char(string='Department')
    hire_date = fields.Date(string='Hire Date')