# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
       This is an Hospital Management application""",

    'description': """
        This is an Hospital Management application which is developed for manage all hospital needs.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_view.xml',
        'data/Seq.xml',
        'data/ConsultSeq.xml',
        'data/MedicineSeq.xml',
        'data/AppointmentSeq.xml',
        'views/res_partner_view.xml',
        'views/hospital_op_view.xml',
        'views/hospital_consultation.xml',
        'views/hospital_diseases_view.xml',
        'views/hr_employee.xml',
        'views/hospital_medicine_view.xml',
        'views/hospital_appointment_view.xml',
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
