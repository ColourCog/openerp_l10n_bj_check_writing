#-*- coding:utf-8 -*-
{
    'name': 'Benin - Check Writing',
    'category': 'Accounting',
    'author': 'ColourCog.com',
    'depends': [
        'account_check_writing',
    ],
    'version': '1.2',
    'description': """
Benin Check Writing.
===========================
This module create printable checks for the major banks in benin.
Currently implemented banks are:

* Bank Of Africa
* BGFI
* UBA
* EcoBank
* Société Générale
* Banque Atlantique
* Diamond Bank
* BSIC
    """,
    'data':[
        'account_check_writing_report.xml',
    ],
    "installable": True,
    "auto_install": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
