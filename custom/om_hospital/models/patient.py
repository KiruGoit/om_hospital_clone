from odoo import api,fields, models,_
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']

    _description = "Patient Master"


    name = fields.Char(string="Patient Name", required=True,
                       tracking=True
                       )
    date_of_birth = fields.Date(string="Date Of Birth",tracking=True )
    gender = fields.Selection([('male', "Male"), ('female', "Female")], string='Gender')
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    is_minor = fields.Boolean(string="Minor")
    guardian = fields.Float(string="Guardian")
    is_pretty = fields.Boolean(string="Pretty")
    def unlink(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointment = self.env['hospital.appointment'].search(domain)
            if appointment:
                raise ValidationError(_('you can not delete the patient...\n %s has an appointment አስገራሚ እውነታዎች',rec.name ))
        return super().unlink()