import camelot
file = "100.pdf"
 
tables = camelot.read_pdf(file, pages = "1-end")
tables.export("camelot_tables.csv", f = "csv")