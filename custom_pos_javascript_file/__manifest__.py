# -*- coding: utf-8 -*-
{
    'name': "POS Javascript",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "SOKAMBY Jesus",
    'website': "http://www.karizma-conseil.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    'assets': {
        'point_of_sale.assets': [
            'custom_pos_javascript_file/static/src/js/custom_pos.js',
        ],
        'web.assets_qweb': [
            'custom_pos_javascript_file/static/src/xml/pos_screen.xml',
            'custom_pos_javascript_file/static/src/xml/display_client.xml',
        ],
    },

    # always loaded
    # 'data': [
    #     'security/security.xml',
    #     'security/ir.model.access.csv',
    #     'data/seq_data.xml',
    #     'views/menu.xml',
    #     'views/medical_file_views.xml',
    #     'views/hr_employee_medical_view.xml',
    # ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': 'False',
    'sequence': -100,
}
