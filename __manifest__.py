# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'OstroVit App',
    'version': 'v1.0',
    'summary': 'business app',
    'sequence': 1,
    'description': """ Alien Software""",
    'category': 'productivity',
    'website': '',
    'images': [],
    'author': "Chau Nguyen",
    'depends': ['base', 'sale','mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/sale_order_inherit.xml',
        'views/list_code.xml',
        'views/product_template_inherit.xml',
        # 'views/templates.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}