from odoo import models, fields, api


class HangHoa(models.Model):
    _name = 'kho.hanghoa'
    _description = 'Hàng Hoá'

    mahh = fields.Char(string='Ma Hang Hoa', required=True)
    maloai = fields.Char(string='Ma Loai', required=True)
    idkho = fields.Char(string='ID Kho')
    mavt = fields.Char(string='Mã Vị Trí')
    makh = fields.Char(string='Mã Khách Hàng')
    tenhh = fields.Char(string='Tên Hàng Hoá')

