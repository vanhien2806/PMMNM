from odoo import models, fields, api


class Kho(models.Model):
    _name = 'kho.Kho'
    _description = 'kho'

    idkho = fields.Char(string='ID kho', required=True)
    maloai = fields.Char(string='Ma Loai')
    soluong = fields.Integer(string='So Luong')
