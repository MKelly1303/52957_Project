import mysql.connector
import dbconfig as cfg
class PatientDAO:
	db=""
	def connectToDB(self):
		self.db = mysql.connector.connect(
			host=cfg.mysql['host'],
			username=cfg.mysql['username'],
			password=cfg.mysql['password'],
			database=cfg.mysql['database']
		)
	def __init__(self):
		self.connectToDB()
		
	def getCursor(self):
		if not self.db.is_connected():
			self.connectToDB()
		return self.db.cursor()
		
	def create (self, values):
		cursor = self.getCursor()
		sql="insert into patientinfo (Patients_Name, Patients_Doctor, Patients_Address, Patients_Age) values (%s, %s, %s, %s)"
		cursor.execute(sql, values)

		self.db.commit()
		lastRowId=cursor.lastrowid
		cursor.close()
		return lastrowid
		
	def getAll(self):
		cursor = self.getCursor()
		sql="select * from patientinfo"
		cursor.execute(sql)
		results = cursor.fetchall()
		returnArray = []
		for result in results:
			print(result)
			returnArray.append(self.convertToDictionary(result))
		cursor.close()
		return returnArray
		
	def findByID(self, id):
		cursor = self.getCursor()
		sql="select * from patientinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		result = cursor.fetchone()
		patient.self.convertToDictionary(result)
		cursor.close()
		return self.convertToDictionary(result)
	
	def update(self, values):
		cursor = self.getCursor()
		sql="update patientinfo set Patients_Name= %s, Patients_Doctor= %s, Patients_Address= %s, Patients_Age= %s where id= %s"
		cursor.execute(sql, values)
		self.db.commit()
		cursor.close()
	
	def delete(self, id):
		cursor = self.getCursor()	
		sql="delete from patientinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		self.db.commit()
		cursor.close()
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
		
		