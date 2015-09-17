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
        if len(amount) < 120:
            stars = 120 - len(amount)
            return ' '.join([amount,'*'*stars])

        else: return amount
            
report_sxw.report_sxw(
    'report.account.print.check.benin.boa',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_boa.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.bgfi',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_bgfi.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.sg',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_sg.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.diamond',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_diamond.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.atlantique',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_atlantique.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.bsic',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_bsic.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.uba',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_uba.rml',
    parser=report_print_check_benin,header=False
)
report_sxw.report_sxw(
    'report.account.print.check.benin.ecobank',
    'account.voucher',
    'addons/l10n_bj_check_writing/report/check_benin_ecobank.rml',
    parser=report_print_check_benin,header=False
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
