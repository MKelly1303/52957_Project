import mysql.connector
class PatientDAO:
	db=""
	def __init__(self):
		self.db = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		database="patientdb"
		)
	def create (self, values):
		cursor = self.db.cursor()
		sql="insert into patientinfo (Patients_Name, Patients_Doctor, Patients_Address, Patients_Age) values (%s, %s, %s, %s)"
		cursor.execute(sql, values)

		self.db.commit()
		return cursor.lastrowid
		
	def getAll(self):
		cursor = self.db.cursor()
		sql="select * from patientinfo"
		cursor.execute(sql)
		results = cursor.fetchall()
		returnArray = []
		for result in results:
			returnArray.append(self.convertToDictionary(result))
		return returnArray
		
	def findByID(self, id):
		cursor = self.db.cursor()
		sql="select * from patientinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		result = cursor.fetchone()
		return self.convertToDictionary(result)
	
	def update(self, values):
		cursor = self.db.cursor()
		sql="update patientinfo set Patients_Name= %s, Patients_Doctor= %s, Patients_Address= %s, Patients_Age= %s where id= %s"
		cursor.execute(sql, values)
		self.db.commit()
	
	def delete(self, id):
		cursor = self.db.cursor()	
		sql="delete from patientinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		self.db.commit()
		print("delete done")
		
	def convertToDictionary(self, result):
		colnames=['id','Patients_Name', 'Patients_Doctor', 'Patients_Address', 'Patients_Age']
		print(colnames)
		item = {}
		
		if result: #if result is not empty do this..
			for i, colName in enumerate(colnames):
				print(colName)
				value = result[i]
				item[colName] = value
		
		return item

patientDAO = PatientDAO()
		
		