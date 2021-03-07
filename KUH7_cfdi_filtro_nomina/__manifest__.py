# -*- coding: utf-8 -*-
{
    'name': "KUH7 CFDI Filtro de nómina",
    'version': '1.0',
    'depends': [
        'l10n_mx_sat_sync_itadmin',
    ],
    'website': '',
    'author': "KUH7 Soluciones",
    'category': 'Accounting',
    'description': """
        Filtra las descargas del administrador de documentos digitales y quita los del tipo de nóminas de empleados.
    """,
    # data files always loaded at installation
    'data': [
        'view/add_tree_view.xml',
    ],
}