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
        'security/security.xml',
        'data/appointment_sequence.xml',
        'data/patient_sequence.xml',
        'data/patient_data.xml',
        'views/patients.xml',
        'views/appointment.xml',
        'views/doctors.xml',
        'report/patient_report.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1
}
