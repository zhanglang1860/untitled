
from docxtpl import *
import xlrd

def read_docx(path):
    tpl = DocxTemplate(r'C:\Users\Administrator\PycharmProjects\untitled\files\华润template.docx')
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\PycharmProjects\untitled\files\风资源工作簿-zyc修改.xlsm')
    sheet2 = workbook.sheet_by_name('风电场概况')
    number_of_tower=sheet2.cell(14, 2).value
    context = {'number_of_tower': number_of_tower,
               }

    tpl.render(context)
    tpl.save(r'C:\Users\Administrator\PycharmProjects\untitled\files\chapter5_test.docx')

if __name__ == "__main__":
    read_docx(r'C:\Users\Administrator\PycharmProjects\untitled\files\testA_01.docx')