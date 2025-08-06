{
    'name': 'HR Employee',
    'version': '1.0',
    'summary': 'Manage employee records',
    'description': 'Custom HR module to manage employees',
    'author': 'Your Name',
    'category': 'Human Resources',
    'depends': ['base','hr'],
    'data': [
        'views/employee_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
