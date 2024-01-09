from odoo import models


class PatientCardXls(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("Generate XLSX Report Lines: ", lines)
        print("Generate XLSX Report Data: ", data)
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 12, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Patient Card')
        sheet.write(2, 2, 'name', format1)
        sheet.write(2, 3, lines.patient_name, format2)