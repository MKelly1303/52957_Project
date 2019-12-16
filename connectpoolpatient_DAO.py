import mysql.connector
import dbconfig as cfg
class PatientDAO:
	db=""
	def initConnectToDB(self):
		db = mysql.connector.connect(
			host=cfg.mysql['host'],
			username=cfg.mysql['username'],
			password=cfg.mysql['password'],
			database=cfg.mysql['database'],
			pool_name="my_connection_pool",
			pool_size=10
		)
		return db
	
	def getConnection(self):
		db = mysql.connector.connect(
			pool_name='my_connection_pool'
		)
		return db
		
	def __init__(self):
		db=self.initConnectToDB()
		db.close()
		
	def getCursor(self):
		if not self.db.is_connected():
			self.connectToDB()
		return self.db.cursor()
		
	def create (self, values):
		db = self.getConnection()
		cursor = db.cursor()
		sql="insert into patientinfo (Patients_Name, Patients_Doctor, Patients_Address, Patients_Age) values (%s, %s, %s, %s)"
		cursor.execute(sql, values)

		self.db.commit()
		lastRowId=cursor.lastrowid
		db.close()
		return lastrowid
		
	def getAll(self):
		db = self.getConnection()
		cursor = db.cursor()
		sql="select * from patientinfo"
		cursor.execute(sql)
		results = cursor.fetchall()
		returnArray = []
		for result in results:
			print(result)
			returnArray.append(self.convertToDictionary(result))
		db.close()
		return returnArray
		
	def findByID(self, id):
		db = self.getConnection()
		cursor = db.cursor()
		sql="select * from patientinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		result = cursor.fetchone()
		patient.self.convertToDictionary(result)
		db.close()
		return self.convertToDictionary(result)
	
	def update(self, values):
		db = self.getConnection()
		cursor = db.cursor()
		sql="update patientinfo set Patients_Name= %s, Patients_Doctor= %s, Patients_Address= %s, Patients_Age= %s where id= %s"
		cursor.execute(sql, values)
		self.db.commit()
		db.close()
	
	def delete(self, id):
		db = self.getConnection()
		cursor = db.cursor()	
		sql="delete from patientinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		self.db.commit()
		db.close()
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
		
		