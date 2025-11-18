{
    "name": "hospital Management System",
    "author": "Kiru Odoo wizard",
    "license": "LGPL-3",
    "version": "17.0.1.1",
    "depends": [
        'mail',
        'product',
        'account'
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        "data/sequence.xml",
        "views/appointment_views.xml",
        "views/appointment_line_views.xml",
        "views/patient_readonly_views.xml",
        "views/patient_views.xml",
        "views/patient_tag_views.xml",
        "views/account_move_views.xml",
        "views/menu.xml"
    ]
}
