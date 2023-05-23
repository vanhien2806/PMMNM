from odoo import models, fields, api


class KhachHang(models.Model):
    _name = 'kho.khachhang'
    _description = 'Khách Hàng'

    makh = fields.Char(string='Ma Khach Hang', required=True)
    ten = fields.Char(string='Ten Khach Hang', required=True)
    diachi = fields.Char(string='Dia Chi')
    sdt = fields.Char(string='So Dien Thoai')

