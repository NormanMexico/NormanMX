# -*- encoding: utf-8 -*-
from datetime import datetime
from dateutil import relativedelta
import pytz

from odoo import models, api, fields

class HrContract(models.Model):
    _inherit = 'hr.contract'

    @api.model
    def _difference_date(self, init_date):
        fmt = '%Y-%m-%d'
        start_date = init_date.strftime(fmt)
        end_date = datetime.now(pytz.timezone('America/Mexico_City')).strftime(fmt)
        # Pasamos a una lista cada fecha para poder manipular cada dato
        a_end_date = end_date.split('-')
        a_start_date = start_date.split('-')
        # Evaluamos a tiempo las dos fechas para validar si una es mayor a otra
        d1 = datetime.strptime(start_date, fmt)
        d2 = datetime.strptime(end_date, fmt)
        # Validamos si la fecha actual es mayor a la fecha de alta
        if d2 > d1:
            date1 = datetime(int(a_start_date[0]), int(a_start_date[1]), int(a_start_date[2]))
            date2 = datetime(int(a_end_date[0]), int(a_end_date[1]), int(a_end_date[2]))

            diff = relativedelta.relativedelta(date2, date1)

            year = diff.years
            months = diff.months
            days = diff.days

            return str(year) + " AÑOS " + str(months) + " MESES " + str(days) + " DÍAS"
        else:
            return "0 AÑOS 0 MESES 0 DÍAS"