# -*- coding: utf-8 -*-
import xlrd
import sys 


if __name__ == "__main__": 

	filename = sys.argv[1]
	
	# 打开文件
	data = xlrd.open_workbook(filename)
	
	# 查看工作表
	sheets = data.sheet_names()

	# 通过文件名获得工作表,获取工作表1
	table = data.sheet_by_name( sheets[0] )

	for i_row in range( table.nrows ):
		print( "\t".join( map( lambda x: str(int(x)) if isinstance(x,float) else x, table.row_values( i_row ) ) ) )

