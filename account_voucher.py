#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  account_voucher.py
#  
#  Copyright 2015 Bidossessi Sodonon <bidossessi@linuxbenin.com>

from openerp.osv import osv,fields
from openerp.tools.translate import _
from lxml import etree

class account_voucher(osv.osv):
    _inherit = 'account.voucher'

    def print_check(self, cr, uid, ids, context=None):
        if not ids:
            return  {}

        check_layout_report = {
            'top' : 'account.print.check.top',
            'middle' : 'account.print.check.middle',
            'bottom' : 'account.print.check.bottom',
            'benin-uba' : 'account.print.check.benin.uba',
            'benin-ecobank' : 'account.print.check.benin.ecobank',
        }

        check_layout = self.browse(cr, uid, ids[0], context=context).company_id.check_layout
        return {
            'type': 'ir.actions.report.xml', 
            'report_name':check_layout_report[check_layout],
            'datas': {
                    'model':'account.voucher',
                    'id': ids and ids[0] or False,
                    'ids': ids and ids or [],
                    'report_type': 'pdf'
                },
            'nodestroy': True
            }

account_voucher()
