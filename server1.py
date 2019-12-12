#!flask/bin/python
#Mark Kelly - 52957 Data Representation - 2019
from flask import Flask, jsonify, request, abort
from patient_DAO import patientDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/patients"


@app.route('/patients')
def getAll():
	patient_results = patientDAO.getAll()
	return jsonify(patient_results)
	
	
	
 
#curl "http://127.0.0.1:5000/patients/3" for testing
@app.route('/patients/<int:id>')
def findById(id):
	foundPatients = patientDAO.findByID(id)
	return jsonify(foundPatients)
	
	
	
# curl -i -H "Content-Type:application/json" -X Post -d "{\"Patients_Name\":\"Florence Kelly\",\"Patients_Doctor\":\"Doctor Smith\",\"Patients_Address\":\"High Street, Dublin\",\"Patients_Age\":19}" http://127.0.0.1:5000/patients
@app.route('/patients', methods=['POST'])
def create():
	if not request.json:
		abort(400)
	#if not 'Patients_Name' in request.json:
	#	abort(400)
	patient = {
		"Patients_Name": request.json['Patients_Name'],
		"Patients_Doctor": request.json['Patients_Doctor'],
		"Patients_Address": request.json['Patients_Address'],
		"Patients_Age": request.json['Patients_Age'],
	}
	values =(patient['Patients_Name'],patient['Patients_Doctor'],patient['Patients_Address'], patient['Patients_Age'])
	newId = patientDAO.create(values)
	patient['id'] = newId
	return jsonify(patient)
	
	
	


#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Patients_Name\":\"Florence Welsh\",\"Patients_Doctor\":\"Doctor Smith\",\"Patients_Address\":\"High Street, Dublin\",\"Patients_Age\":20}" http://127.0.0.1:5000/patients/4
@app.route('/patients/<int:id>', methods=['PUT'])
def update(id):
	foundPatients = patientDAO.findByID(id)
	if not foundPatients:
		abort(404)
	if not request.json:
		abort(400)
	reqJson = request.json
	if 'Patients_Age' in reqJson and type(reqJson['Patients_Age']) is not int:
		abort(400)
	if 'Patients_Name' in reqJson:
		foundPatients['Patients_Name'] = reqJson['Patients_Name']
	if 'Patients_Doctor' in reqJson:
		foundPatients['Patients_Doctor'] = reqJson['Patients_Doctor']
	if 'Patients_Address' in reqJson:
		foundPatients['Patients_Address'] = reqJson['Patients_Address']
	if 'Patients_Age' in reqJson:
		foundPatients['Patients_Age'] = reqJson['Patients_Age']
	values =(foundPatients['Patients_Name'],foundPatients['Patients_Doctor'],foundPatients['Patients_Address'], foundPatients['Patients_Age'], foundPatients['id'])
	patientDAO.update(values)
	return jsonify(foundPatients)
	



#curl -X DELETE "http://127.0.0.1:5000/patients/1"
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete(id):
	patientDAO.delete(id)
	return jsonify({"Deletion Completed": True})





 
if __name__ == '__main__' :
 app.run(debug= True)
