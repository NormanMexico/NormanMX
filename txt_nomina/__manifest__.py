# -*- coding: utf-8 -*-
{
    'name': "Genera TXT de Nomina",
    'version': '1.0',
    'depends': [
        'nomina_cfdi_ee',
    ],
    'website': '',
    'author': "Jorge Diaz",
    'category': 'Tools',
    'description': """
        Este modulo genera archivo TXT de Nomina de los Empleados
    """,
    # data files always loaded at installation
    'data': [
        'view/view_txt_nomina.xml',
    ],
}
