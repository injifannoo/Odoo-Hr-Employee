# from odoo import models, fields
# from datetime import datetime

# class Attendance(models.Model):
#     _name = 'x_hr.attendance'
#     _description = 'Attendance'

#     employee_id = fields.Many2one('hr.employee', required=True)
#     check_in = fields.Datetime(default=lambda self: fields.Datetime.now())
#     check_out = fields.Datetime()