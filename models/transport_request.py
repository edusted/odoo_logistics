from odoo import models, fields, api

class TransportRequest(models.Model):
    _name = 'logistics.transport_request'
    _description = 'Transport Request'

    name = fields.Char(string='Request Name', required=True)
    request_type = fields.Many2one('logistics.request_type', string='Request Type')  
    sender_name = fields.Char(string='Sender Name')  
    sender_contact = fields.Char(string='Sender Contact')  
    receiver_name = fields.Char(string='Receiver Name')  
    receiver_contact = fields.Char(string='Receiver Contact')  
    responsible_manager = fields.Char(string='Responsible Manager')  
    responsible_logistician = fields.Char(string='Responsible Logistician')  
    date_request = fields.Date(string='Request Date', default=fields.Date.context_today)
    comment = fields.Text(string='Comment')
    package_type_id = fields.Many2one('logistics.packaging_type', string='Package Type')  
    package_qty = fields.Integer(string='Package Quantity')
    priority_id = fields.Many2one('logistics.priority_type', string='Priority')  
    total_weight = fields.Float(string='Total Weight')
    total_volume = fields.Float(string='Total Volume')
    expense_category_id = fields.Many2one('logistics.expense_category', string='Expense Category')  
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('canceled', 'Canceled')
    ], string='Status', default='draft')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('logistics.transport_request') or 'New'
        return super(TransportRequest, self).create(vals)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'canceled'
