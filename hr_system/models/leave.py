# from odoo import models, fields

# class LeaveRequest(models.Model):
#     _name = 'x_hr.leave'
#     _description = 'Leave Request'

#     employee_id = fields.Many2one('hr_system.employee', required=True)
#     start_date = fields.Date(required=True)
#     end_date = fields.Date(required=True)
#     reason = fields.Text()
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected')
#     ], default='draft')