{
    'name': 'Hospital Management',
    'version': '13.0.0.0.1',
    'category': 'Healthcare',
    'summary': 'Hospital Management System',
    'description': 'This module provides a complete solution for managing a hospital.',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_sequence.xml',
        'views/patients.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1
}
