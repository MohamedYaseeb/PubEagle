from odoo import models, fields, api, _
from datetime import datetime, date


class InheritStockAdjustment(models.Model):
    _inherit = 'stock.quant'

    lot_expiry = fields.Date(string='Expiray Date')
    lot_id = fields.Many2one(
        'stock.lot', 'Lot/Serial Number', index=True,
        ondelete='restrict', check_company=True,
        domain=lambda self: self._domain_lot_id(), required=True)





    @api.model
    def _get_inventory_fields_create(self):
        """ Returns a list of fields user can edit when he want to create a quant in `inventory_mode`.
        """
        return ['product_id', 'location_id', 'lot_id', 'package_id', 'owner_id','lot_expiry'] + self._get_inventory_fields_write()




    @api.onchange('lot_expiry')
    def compute_expiry(self):
        adjust_obj = self.env['stock.lot']
        search_obj = adjust_obj.search([])
        for obj in search_obj:
            if self.lot_id.name == obj.name:
                self.lot_id.expiration_date = self.lot_expiry



class StockProductionLotInheritanve(models.Model):
    _inherit = 'stock.lot'


    expiration_date = fields.Datetime(string='Expiration Date')


