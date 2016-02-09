# -*- encoding: utf-8 -*-
##############################################################################
#
#    Mandate module for openERP
#    Copyright (C) 2014 Compassion CH (http://www.compassion.ch)
#    @author: Cyril Sester <csester@compassion.ch>,
#             Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    mandate_ids = fields.One2many(
        comodel_name='account.banking.mandate', inverse_name='partner_bank_id',
        string='Direct Debit Mandates',
        help='Banking mandates represents an authorization that the bank '
             'account owner gives to a company for a specific operation')

    acc_masked = fields.Char(
        string='Masked account', store=True, readonly=True,
        compute='_compute_acc_masked')

    @api.depends('acc_number')
    def _compute_acc_masked(self):
        for bank in self:
            acc_number = bank.acc_number
            if len(acc_number) > 4:
                self.acc_masked = acc_number[-4:].rjust(len(acc_number), "*")
            else:
                self.acc_masked = False
