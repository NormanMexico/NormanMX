# -*- coding:utf-8 -*-

import base64
import io
import pytz
from odoo import api, fields, models
from datetime import datetime
from decimal import Decimal

class GeneraTxt(models.Model):
    _inherit = 'hr.payslip.run'

    filecontent = fields.Binary(string='Archivo')
    Fecha_TXT = datetime.now(pytz.timezone('America/Mexico_City')).strftime('%Y-%m-%d %H:%M:%S')


    def generate_file(self):
        #txt_total = fields.One2many('hr.payslip', 'employee_id', string='Payslips', readonly=True)
        #txt_total = 'HOLA MUNDO \r\nHOLA MUNDO'
        v_contador = 1
        txt_total = ''

        newslip_ids = sorted(self.slip_ids, key=lambda num : num.employee_id.no_empleado)
        for record in newslip_ids:
            no_cuenta = record.employee_id.no_cuenta
            empleado = record.employee_id.name

            re_empleado = str(empleado).replace('Ñ', 'N')

            r_Total_Salario = ''
            #print("Texto Extraido", record.name)
            for record2 in record.line_ids:
                if record2.code == 'EFECT':
                    total_salario = record2.total
                    d_total_salario = Decimal(total_salario)
                    q_decimal_Total_Salario = round(d_total_salario, 2)
                    v_Total_Salario = str(q_decimal_Total_Salario).split('.')
                    #print("Texto Extraido", record2.amount)
                    r_Total_Salario = v_Total_Salario[0] + v_Total_Salario[1]

            if no_cuenta is False:
                errorData = ("Se elimino un dato del .txt de la persona" + " " + re_empleado + " " + "Porque no tiene número de cuenta...")
                print(errorData)
            else:
                txt_total += str(v_contador).rjust(9, '0') + '                ' + '99' + str(no_cuenta) + '          ' + str(r_Total_Salario).rjust(15, '0') + (re_empleado).ljust(39, ' ') + ' ' + '001001\r\n'
                v_contador += 1


        output = io.BytesIO(io.StringIO(txt_total).read().encode('utf8'))
        self.filecontent = base64.b64encode(output.read())
        filename_field = ('Nomina_Empleados_{0}'.format(self.Fecha_TXT))
        if self.filecontent:
            return {
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': (
                    'web/content/?model=hr.payslip.run&id={0}'
                    '&filename_field={1}'
                    '&field=filecontent&download=true'
                    '&filename={1}.txt'.format(
                        self.id,
                        filename_field,
                    )
                )
            }


