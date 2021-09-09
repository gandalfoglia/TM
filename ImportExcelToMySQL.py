import xlrd
import mysql.connector

# Open the workbook and define the worksheet
book = xlrd.open_workbook("divorces (copy).xls")
sheet = book.sheet_by_name("divorces")

# Establish a MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="Travail_Maturite2021",
  database="statistiques"
)
# Get the cursor, which is used to traverse the database, line by line
mycursor = mydb.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO divorce (Cantons, Total, SS, SEE, ESE, EE) VALUES (%s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		Cantons		= sheet.cell(r,0).value
		Total       = sheet.cell(r,1).value
		SS			= sheet.cell(r,2).value
		SEE		    = sheet.cell(r,3).value
		ESE		    = sheet.cell(r,4).value
		EE		    = sheet.cell(r,5).value

		# Assign values from each row
		values = (Cantons, Total, SS, SEE, ESE, EE)

		# Execute sql Query
		mycursor.execute(query, values)


# Close the cursor
mycursor.close()

# Commit the transaction
mydb.commit()

# Close the database connection
mydb.close()

# Print results
print ("")
print ("All Done! Bye, for now.")
print ("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("I just imported " + columns + " columns and " + rows + " rows to MySQL!")
