# -*- coding: utf-8 -*-

import xlwt
import io
from xlwt import easyxf
import pytz
from datetime import date
from datetime import datetime
from collections import defaultdict
from odoo import models, fields, api

class WizardReporteIsn(models.TransientModel):
    _name = 'wizard.reporte.isn'
    _description = 'Reporte2%ISN'

    name = fields.Char(string="Name")
    file_data = fields.Binary("File Data")
    from_date = fields.Date(string="From date", required=True)
    to_date = fields.Date(string="To date", required=True)

    @api.model
    def _default_year(self):
        tz_MX = pytz.timezone('America/Mexico_City')
        today = datetime.now(tz_MX)
        year = today.strftime('%Y')
        return year

    year = fields.Char(string="Year", required=True, default=_default_year)

    @api.model
    def _default_company(self):
        return 1

    company_id = fields.Many2one(string="Company", comodel_name="res.company", required=True, default=_default_company)

    def print_isn_report(self):
        #periodo = int(self.no_period)
        #year = self.year
        #start_range = year + "-" + str(self.no_period) + "-01"
        start_range = self.from_date
        #months = ["*", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
        #estados = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Chiapas', 'Chihuahua',
        #           'Coahuila', 'Colima', 'Ciudad de México', 'Durango', 'México', 'Guanajuato', 'Guerrero', 'Hidalgo',
        #           'Jalisco', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro',
        #           'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala',
        #           'Veracruz', 'Yucatán', 'Zacatecas']
        #porcentaje = [2.50, 3.00, 2.50, 2.00, 2.00, 3.00, 2.00, 2.00, 3.00, 2.00, 3.00, 2.30, 2.00, 2.50, 2.00, 3.00,
        #              2.00, 2.00, 3.00, 3.00, 3.00, 2.00, 3.00, 2.50, 2.40, 2.00, 2.50, 3.00, 3.00, 3.00, 2.50, 2.50]

        #pos = int(str(self.no_period)) * 1
        #print("Tipo dato", type(pos))

        #if periodo == 1 or periodo == 3 or periodo == 5 or periodo == 7 or periodo == 8 or periodo == 10 or periodo == 12:
        #    end_range = year + "-" + str(self.no_period) + "-31"
        #elif periodo == 4 or periodo == 6 or periodo == 9 or periodo == 11:
        #    end_range = year + "-" + str(self.no_period) + "-30"
        #else:
        #    end_range = year + "-" + str(self.no_period) + "-28"

        end_range = self.to_date

        #id_department = self._context.get('department')
        id_company = self.company_id
        domain = [('state', '=', 'done')]
        if start_range:
            domain.append(('date_from', '>=', start_range))
        if end_range:
            domain.append(('date_to', '<=', end_range))
        if id_company:
            domain.append(('company_id', '=', id_company.id))
        #    employees = self.env['hr.employee'].search([('department_id', '=', id_department.id)])
        #    domain.append(('employee_id', 'in', employees.ids))

        payslips = self.env['hr.payslip'].search(domain)
        struct_salary = self.env['hr.payroll.structure'].search([('name', '=', 'SEMANAL')])
        #rules = self.env['hr.salary.rule'].search([('active', '=', True)])
        rules = struct_salary.mapped('rule_ids')
        #payslip_lines = payslips.mapped('line_ids').filtered(lambda x: x.salary_rule_id.id in rules.ids)  # .sorted(key=lambda x: x.slip_id.employee_id)
        payslip_lines = payslips.mapped('line_ids').sorted(key=lambda x: x.slip_id.employee_id.department_id.name)

        import base64
        workbook = xlwt.Workbook()

        worksheet = workbook.add_sheet('2% ISN', cell_overwrite_ok=True)

        text_bold_left_title = easyxf('font:height 300; align: horiz center; font:bold True;')
        text_bold_left_subtitle = easyxf('font:height 250; align: horiz center;')
        text_bold_left_subtitle_b = easyxf('font:height 230; align: horiz center; font:bold True;')
        text_bold_left_paragrah = easyxf('font:height 160; align: horiz left;')
        text_bold_center_paragrah = easyxf('font:height 160; align: horiz center;')

        tz_MX = pytz.timezone('America/Mexico_City')
        now = datetime.now(tz_MX)
        today = date.today()

        money_format = xlwt.XFStyle()
        money_format.num_format_str = '$#,##0.00'
        money_format.font.height = 180
        money_format.alignment.HORZ_RIGHT = True

        money_format_b = xlwt.XFStyle()
        money_format_b.num_format_str = '$#,##0.00'
        money_format_b.font.height = 180
        money_format_b.font.bold = True
        money_format_b.alignment.HORZ_RIGHT = True

        money_format_n = xlwt.XFStyle()
        money_format_n.num_format_str = '#,##0.00'
        money_format_n.font.height = 180
        money_format_n.alignment.HORZ_RIGHT = True

        font_format = xlwt.XFStyle()
        font_format.font.height = 180
        font_format.alignment.HORZ_LEFT = True

        font_format_r = xlwt.XFStyle()
        font_format_r.font.height = 180
        font_format_r.alignment.HORZ_RIGHT = True

        font_format_r_b = xlwt.XFStyle()
        font_format_r_b.font.height = 180
        font_format_r_b.font.bold = True
        font_format_r_b.alignment.HORZ_RIGHT = True

        font_format_l_b = xlwt.XFStyle()
        font_format_l_b.font.height = 180
        font_format_l_b.font.bold = True
        font_format_l_b.alignment.HORZ_LEFT = True

        font_format_h = xlwt.XFStyle()
        font_format_h.font.height = 150
        font_format_h.font.bold = True
        font_format_h.alignment.wrap = True
        font_format_h.alignment.HORZ_CENTER = True

        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = xlwt.Style.colour_map['light_yellow']
        font_format_h.pattern = pattern

        border = xlwt.Borders()
        border.left = 1
        border.right = 1
        border.top = 2
        border.bottom = 2
        border.right_colour = xlwt.Style.colour_map['blue']
        border.left_colour = xlwt.Style.colour_map['blue']
        border.top_colour = xlwt.Style.colour_map['blue']
        border.bottom_colour = xlwt.Style.colour_map['blue']
        font_format_h.borders = border

        col = 3
        rule_index = {}
        codes_rules = []
        #print("reglas", rules)
        for rule in rules:
            if rule.category_id.code == "ALW" or rule.code == "TPER" or rule.code == "PO01" or rule.code == "P003":
                worksheet.write(5, col, rule.name, font_format_h)
                rule_index.update({rule.id: col})
                col += 1
                codes_rules.append(rule.code)
        #print("index", rule_index)
        #worksheet.write(5, col, 'DEPARTAMENTO', font_format_h)
        worksheet.write(5, col, 'ISN', font_format_h)
        #worksheet.write(5, col + 2, 'ESTADO', font_format_h)
        from_to_date = 'Periodo de  %s A %s' % (start_range or '', end_range or '')
        concepto = 'Concepto:  %s' % (start_range)

        #print("ISN", 'ISN ' + months[9])

        #period = 'Periodo del ' + self.date_start.strftime('%d/%m/%Y') + ' al ' + self.date_end.strftime('%d/%m/%Y')
        worksheet.write_merge(0, 0, 1, 5, id_company.name, text_bold_left_title)
        worksheet.write_merge(2, 2, 1, 5, 'REPORTE 2% ISN', text_bold_left_subtitle)
        worksheet.write_merge(3, 3, 1, 5, from_to_date, text_bold_center_paragrah)

        worksheet.write_merge(2, 2, 6, 8, 'Hora :' + now.strftime("%H:%M:%S"), text_bold_left_paragrah)
        worksheet.write_merge(3, 3, 6, 8, 'Fecha :' + today.strftime("%d/%m/%Y"), text_bold_left_paragrah)

        worksheet.write(5, 0, 'Código', font_format_h)
        worksheet.write(5, 1, 'Empleado', font_format_h)
        worksheet.write(5, 2, 'Departamento', font_format_h)

        # employees = defaultdict(dict)
        # employee_payslip = defaultdict(set)
        employees = {}
        for line in payslip_lines:
            if line.slip_id.employee_id not in employees:
                employees[line.slip_id.employee_id] = {line.slip_id: []}
            if line.slip_id not in employees[line.slip_id.employee_id]:
                employees[line.slip_id.employee_id].update({line.slip_id: []})
            employees[line.slip_id.employee_id][line.slip_id].append(line)

            # employees[line.slip_id.employee_id].add(line)

            # employee_payslip[line.slip_id.employee_id].add(line.slip_id)

        row = 6
        #tipo_nomina = {'O1': 'DIARIO', 'O2': 'SEMANAL', 'O3': 'CATORCENAL', 'O4': 'QUINCENAL', 'O5': 'MENSUAL', '': 'SIN TIPO DE NOMINA'}
        for employee, payslips in employees.items():
            worksheet.write(row, 1, employee.name, font_format)
            worksheet.write(row, 0, employee.no_empleado, font_format)
            worksheet.write(row, 2, employee.department_id.name, font_format)
            #row += 1
            #worksheet.write(row, 1, 'Fecha de la nomina', bold)
            #worksheet.write(row, 2, 'Tipo', bold)
            #row += 1
            total_by_rule = defaultdict(lambda: 0.0)
            #print("totales", total_by_rule)
            #codes_rules.append(rule.code)
            amt_rules = []
            for x in range(0, len(codes_rules)):
                amt_rules.append(0.00)

            total_antes_isn = 0.00

            for payslip, lines in payslips.items():
                # for line in lines:
                #worksheet.write(row, 1, payslip.date_from)
                #worksheet.write(row, 2, tipo_nomina.get(payslip.tipo_nomina, ''))
                for x in range(0, len(codes_rules)):
                    if codes_rules[x] == 'TPER':
                        total_antes_isn += line.total
                    for line in lines:
                        if codes_rules[x] == line.code:
                            amt_rules[x] += line.total
                            break
                #for line in lines:
                    #worksheet.write(row, rule_index.get(line.salary_rule_id.id), line.total)
                    #total_by_rule[line.salary_rule_id.id] += line.total
                #row += 1
            #worksheet.write(row, 2, 'Total', bold)
            column = 3
            for total in range(0, len(amt_rules)):
                worksheet.write(row, column, round(amt_rules[total], 2), money_format)
                column += 1
            #for rule_id, total in total_by_rule.items():
            #    print("Total", total)
                #worksheet.write(row, rule_index.get(rule_id), total)

            #porcentaje_isn = 2
            #for isn_porc in range(0, len(estados)):
            #    if employee.estado.name == estados[isn_porc]:
            #        porcentaje_isn = porcentaje[isn_porc]
            #        break

            total_isn = total_antes_isn * 0.023

            #worksheet.write(row, col, employee.department_id.name, font_format)
            worksheet.write(row, col, round(total_isn, 2), money_format)
            #worksheet.write(row, col + 2, employee.estado.name, font_format)
            #worksheet.write(row, 0, employee.name, font_format)
            row += 1

        fp = io.BytesIO()
        workbook.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()

        self.write({'file_data': base64.b64encode(data)})
        action = {
            'name': 'Payslips',
            'type': 'ir.actions.act_url',
            'url': "/web/content/?model=" + self._name + "&id=" + str(
                self.id) + "&field=file_data&download=true&filename=Reporte_2_porciento_isn.xls",
            'target': 'self',
        }
        return action

