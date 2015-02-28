#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  check_print.py
#  
#  Copyright 2015 Bidossessi Sodonon <bidossessi@linuxbenin.com>

import time
from openerp.report import report_sxw

class report_print_check_benin(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_print_check_benin, self).__init__(cr, uid, name, context)
        self.number_lines = 0
        self.number_add = 0
        self.localcontext.update({
            'time': time,
            'fill_pound': self.fill_pound,
            'fill_stars' : self.fill_stars,
        })

    def fill_pound(self, amount):
            return '#'+ amount +'#'

    def fill_stars(self, amount):
        if len(amount) < 140:
            stars = 140 - len(amount)
            return ' '.join([amount,'*'*stars])

        else: return amount
            
report_sxw.report_sxw(
    'report.account.print.check.benin',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin.rml',
    parser=report_print_check_benin,header=False
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
