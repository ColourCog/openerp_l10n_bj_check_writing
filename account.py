#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  account.py
#  
#  Copyright 2015 Bidossessi Sodonon <bidossessi@linuxbenin.com>

from openerp.osv import osv,fields


class res_company(osv.osv):
    _inherit = "res.company"
    _columns = {
        'check_layout': fields.selection([
            ('top', 'Check on Top'),
            ('middle', 'Check in middle'),
            ('bottom', 'Check on bottom'),
            ('benin', 'Benin standard format'),
            ],"Check Layout",
            help="Check on top is compatible with Quicken, QuickBooks and Microsoft Money. Check in middle is compatible with Peachtree, ACCPAC and DacEasy. Check on bottom is compatible with Peachtree, ACCPAC and DacEasy only"  ),
        }
        
    _defaults = {
        'check_layout' : lambda *a: 'benin',
    }
    
res_company()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
