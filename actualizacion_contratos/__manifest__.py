# -*- coding: utf-8 -*-
{
    'name': 'KUH7 - Actualización información de contratos',
    'summary': 'Agregar campos en el apartado de deducciones en el contrato',
    'description': '''
    * Agregar campos de descuento back to school, comedor y lentes
    ''',
    "website": "https://www.kuh7.mx",
    'author': 'KUH7 SOLUCIONES S.A. DE C.V.',
    'version': '1.0',
    'category': 'contract',
    'depends': [
        'nomina_cfdi_ee',
        'nomina_cfdi_extras_ee',
        'hr_contract'
    ],
    'data': [
        'views/hr_contract_view.xml',
    ],
    'installable': True,
    'application': False
}