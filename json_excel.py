import json,xlwt

# 解析json
def readJsonfile():
    jsobj=json.load(open(r'E:/Megene/HCB80040661.json',encoding='UTF-8'))
    return jsobj
#转换为excel

jsonfile=readJsonfile()
workbook=xlwt.Workbook()
print(len(jsonfile))
#print(jsonfile)
sheet1=workbook.add_sheet('类型')
Row=column=0
sheet1.write(Row,column,'类型')
column=column+1
sheet1.write(Row,column,'second_level')
column=column+1
sheet1.write(Row,column,'top_level')
column=column+1
sheet1.write(Row,column,'conclusion')
column=column+1
sheet1.write(Row,column,'snp')
column=column+1
sheet1.write(Row,column,'result')
column=column+1
sheet1.write(Row,column,'Genotype')
column=column+1
sheet1.write(Row,column,'gene')
column=0
for i in jsonfile.keys():
    species=jsonfile[i]
    Row=Row+1
    sheet1.write(Row,column,i)
    column=column+1
    sheet1.write(Row,column,species['secode-level'])
    column=column+1
    sheet1.write(Row,column,species['top-level'])
    column=column+1
    sheet1.write(Row,column,species['conclusion'])
    column=column+1
    snplist=species['snp']
    for snp in snplist.keys():
        sheet1.write(Row,column,snp)
        column=column+1
        snp_r=snplist[snp]
        for key in snp_r:
            sheet1.write(Row,column,snp_r[key])
            column=column+1
        column=4
        Row=Row+1
    column=0
workbook.save('E:/Megene/Megene.xls')


