# -*- coding: utf-8 -*-
import xlrd
import sys 

# https://www.cnblogs.com/tynam/p/11204895.html 
# usage: python learn_process_xls.py ${filename} 

if __name__ == "__main__": 

	filename = sys.argv[1]
	
	# 打开文件
	data = xlrd.open_workbook(filename)
	
	# 查看工作表
	sheets = data.sheet_names()
	print("sheets: ", sheets )
	print( type( sheets ) )

	# 通过文件名获得工作表,获取工作表1
	table = data.sheet_by_name( sheets[0] ) 
	
	# 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1
	# table = data.sheet_by_index(0)
	# 获取行数和列数
	# 行数：table.nrows
	# 列数：table.ncols
	print("总行数：" + str(table.nrows))
	print("总列数：" + str(table.ncols))
	print( type(table.row_values) ) 
	print( table.row_values )

	# 获取整行的值 和整列的值，返回的结果为数组
	# 整行值：table.row_values(colx, start_rowx=0, end_rowx=None)
	# 整列值：table.col_values(......)
	# 参数 start 为从第几个开始打印，
	# end为打印到那个位置结束，默认为none
	print("整行值：" + str(table.row_values(0)))
	print("整列值：" + str(table.col_values(1)))
	print( table.row_values(1) )
	print( type( table.row_values(0) ) )

	# 获取某个单元格的值，例如获取B3单元格值
	cel_B3 = table.cell(1,9).value
	print("第三行第二列的值：" , cel_B3)






