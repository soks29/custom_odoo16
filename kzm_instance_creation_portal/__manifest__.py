# -*- coding: utf-8 -*-
{
    'name': "KZM Portal",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "SOKAMBY Jesus",
    'website': "https://github.com/soks29/custom_odoo16",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'kzm_instance_request', 'website', 'portal'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_form.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #    'demo/demo.xml',
    # ],
    'sequence': -100,
    'installable': True,
    'application': True,
}
