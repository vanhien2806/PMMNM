from odoo import models, fields, api


class ViTriKho(models.Model):
    _name = 'kho.vitrikho'
    _description = 'Vị Trí Kho'

    mavt = fields.Char(string='Ma Vi Tri', required=True)
    idkho = fields.Char(string='ID Kho', required=True)
    maloai = fields.Char(string='Ma Loai')


