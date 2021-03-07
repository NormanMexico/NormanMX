# -*- encoding: utf-8 -*-
{
    'name': "KUH7 - Reporte de incidencias y gestión de nóminas",
    'summary': 'Reporte de incidencias y 2% de ISN',
    'version': '1.0',
    'depends': [
        'nomina_cfdi_extras_ee',
        'nomina_cfdi_ee',
    ],
    'website': 'https://www.kuh7.mx',
    'author': "KUH7 SOLUCIONES S.A. DE C.V.",
    'category': 'Report',
    'description': """
    * Generar reporte de incidencias de VAC, INC, RET, DFES y HE sobre cada periodo de nómina.
    * Generar reporte de 2% de ISN por mes.
    """,
    'data': [
        'reports/reporte_incidencia_h_e.xml',
        'reports/reporte_incidencias_df.xml',
        'reports/reporte_incidencias_faltas.xml',
        'reports/reporte_incidencias_inc.xml',
        'reports/reporte_incidencias_ret.xml',
        'reports/reporte_incidencias_vac.xml',
        'wizard/wizard_reporte_isn.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False
}