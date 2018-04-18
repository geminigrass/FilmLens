# import os
# import glob
# import csv
# from xlsxwriter.workbook import Workbook

import sys
print(sys.path)

# for csvfile in glob.glob(os.path.join('.', '*.csv')):
#     workbook = Workbook(csvfile[:-4] + '.xlsx')
#     worksheet = workbook.add_worksheet()
#     with open(csvfile, 'rt', encoding='utf8') as f:
#         reader = csv.reader(f)
#         for r, row in enumerate(reader):
#             for c, col in enumerate(row):
#                 worksheet.write(r, c, col)
#     workbook.close()




# #!/usr/bin/env python
# #encoding=utf-8
# import os
# import xlwt
# import csv
#
# def write_execl(csvfile, xlsfile, workbook, sheetname):
#     #创建表名，添加一个workbook的对象
#     sheet = workbook.add_sheet(sheetname)
#     #读取csv文件内容，写入表
#     reader = csv.reader(open(csvfile, 'r'))
#     i = 0
#     for content in reader:
#         for j in range(len(content)):
#             sheet.write(i, j, content[j])
#             j += 1
#         i += 1
#
# #目标execl文件名
# xlsfile = './result.xls'
# #初始化workbook对象
# workbook = xlwt.Workbook()
#
# #创建当前目录下文件列表
# filelist = sorted(os.listdir('./'))
# for file in filelist:
#     #匹配以csv结尾的文件
#     if file.endswith('.csv'):
#         #匹配出表名
#         sheetname = file.replace('.csv', '')
#         #使用函数将csv文件内容导入到execl
#         write_execl(file, xlsfile, workbook, sheetname)
#
# workbook.save(xlsfile)