from odoo import models, fields, api


class HoaDonXuat(models.Model):
    _name = 'kho.hoadonxuat'
    _description = 'Hoá Đơn Xuất'

    sohdxuat = fields.Char(string='So Hoa Don Xuat', required=True)
    makh = fields.Char(string='Ma Khach Hang', required=True)
    manv = fields.Char(string='Ma Nhan Vien')
    ngayxuat = fields.Datetime(string='Ngay Xuat')
    tinhtrangxuat = fields.Char(string='Tinh Trang Xuat')

