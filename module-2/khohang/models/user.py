from odoo import models, fields, api


class User(models.Model):
    _name = 'kho.user'
    _description = 'Người Dùng'

    name = fields.Char(string='Name', required=True)
    password = fields.Char(string='Password', required=True)
    email = fields.Char(string='Email Address')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    phone = fields.Char(string='Phone Number')

