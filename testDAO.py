from connectpoolpatient_DAO import patientDAO as patientDAO

patients = patientDAO.getAll()
for patient in patients:
	print (patient)