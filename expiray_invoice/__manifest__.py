# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Expiray in Invoice',
    'sequence': 1,
    'author' : 'Mohamed Yaseen Dahab',
    'category': 'Accounting/Accounting',
    'summary': 'Add Expiray Date in an Invoice Line',
    'description': """
            ### Module Main Features
            
            1] add lot/serial and Expiration Date in Sale Order Line and Invoice Line
            2] add Expiration Date in Invoice PDF Report
            3] add Expiration Date on Inventory Adjustment Line
            4] Adjust Lot Expiration Date from Inventory Adjustment Lines
    
    
    """,
    'version': '1.0',
    'depends': ['base','stock','product_expiry','sale','account'],
    'data': [
        'views/inherit_invoice.xml',
        'views/inherit_stock.xml',
        'report/inherit_invoice_report.xml'
    ],
    'price': 59,
    'currency' : 'USD',
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}
