# -*- encoding: utf-8 -*-
{
    'name': "KUH7 - Reporte de control de antigüedad del personal",
    'version': '1.1',
    'depends': ['hr_contract', 'nomina_cfdi_extras_ee'],
    'website': 'https://www.kuh7.mx',
    'author': "JOSÉ MARÍA HERIBERTO ALVARADO SOLÓRZANO",
    'category': 'Report',
    'description': """
    Módulo permite generar un reporte general de la antigüedad del personal conforme a la fecha de alta.
    """,
    'data': [
        'report/report_vacaciones_utilizadas_x_empleado.xml',
        'views/contract_historial_salario_view.xml'
    ],
}