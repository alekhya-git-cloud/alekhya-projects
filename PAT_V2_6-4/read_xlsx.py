import xlrd

#fun is used to open_xlsx file
def open_file(file):
	
	wb=xlrd.open_workbook(file)
	sheet=wb.sheet_by_index(0)
	return sheet
	

	
	


