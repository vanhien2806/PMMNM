from odoo import models, fields, api


class Loaihang(models.Model):
    _name = 'kho.loaihang'
    _description = 'Loại Hàng'

    maloai = fields.Char(string='Ma Loai Hang', required=True)
    tenloai = fields.Char(string='Ten Loai Hang')
    tinhtrang = fields.Selection([('con', 'Con'), ('het', 'Het')], string='Con', default='Con')

