from odoo inport models, fields


class BusinessTask(models.Model):
  _name = 'business_task'
  
  
  name = fields.Char(string='Name')
