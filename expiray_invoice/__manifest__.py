# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Expiray in Invoice',
    'sequence': 1,
    'author' : 'Mohamed Yaseen Dahab',
    'category': 'Accounting/Accounting',
    'summary': 'Add Expiray Date in an Invoice Line',
    'description': "Add Expiray Date in Invoice Lines for each Product",
    'version': '1.0',
    'depends': ['base','stock','sale','account'],
    'data': [
        'views/inherit_invoice.xml',
        'report/inherit_invoice_report.xml'
    ],
    'price': 59,
    'currency' : 'USD',
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}
