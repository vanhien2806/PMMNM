from odoo import models, fields,api


class Nhanvien(models.Model):
    _name = 'kho.nhanvien'
    _description = 'Nhân Viên'

    manv = fields.Char(string='Ma Nhan Vien', required=True)
    tennv = fields.Binary(string='Ten Nhan Vien', attachment=True)
    gioitinh = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    ngaysinh = fields.Datetime(string='Ngay Sinh')
    diachi = fields.Char(string='Dia Chi')

