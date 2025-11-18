from odoo import api, fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = "Patient Tag"

    name = fields.Char(string="Patient Tag", required=True, )
    sequence = fields.Integer(default=0)