from odoo import models, fields, api


class HoaDonNhap(models.Model):
    _name = 'kho.hoadonnhap'
    _description = 'Hoá Đơn Nhập'

    sohdnhap = fields.Char(string='So Hoa Don Nhap', required=True)
    makh = fields.Char(string='Ma Khach Hang', required=True)
    manv = fields.Char(string='Ma Nhan Vien')
    ngaynhap = fields.Datetime(string='Ngay Nhap')
    tinhtrangnhap = fields.Char(string='Tinh Trang Nhap')

