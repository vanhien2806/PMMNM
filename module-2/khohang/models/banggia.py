from odoo import models, fields, api


class BangGia(models.Model):
    _name = 'kho.banggia'
    _description = 'Bảng Giá'

    magia = fields.Char(string='Ma Gia', required=True)
    idkho = fields.Char(string='ID Kho', required=True)
    mavt = fields.Char(string='Ma Vi Tri')
    dgtheothang = fields.Char(string='Don Gia Theo Thang')

