#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

patients=[
	{
		"id":1, 
		"Patients_Name":"Harry Browne", 
		"Patients_Doctor":"Doctor Smith",
		"Patients_Address":"1 Sparrow Road, Wicklow",
		"Patients_Age":37
	},
	{
		"id":2, 
		"Patients_Name":"Pamela Jennings", 
		"Patients_Doctor":"Doctor Smith", 
		"Patients_Address":"36 Main Str, Wicklow",
		"Patients_Age":76
	},
	{
		"id":3, 
		"Patients_Name":"Tom Waits", 
		"Patients_Doctor":"Doctor Brennan", 
		"Patients_Address":"Downtown, Dublin",
		"Patients_Age":56
	}
 ]
 
nextId=4 

#curl "http://127.0.0.1:5000/patients"


@app.route('/patients')
def getAll():
	return jsonify(patients)
 
#curl "http://127.0.0.1:5000/patients/3" for testing
@app.route('/patients/<int:id>')
def findById(id):
	foundPatients = list(filter(lambda p: p['id']==id, patients))
	if len(foundPatients ) == 0:
		return jsonify ({}), 204
	return jsonify(foundPatients[0])
	
# curl -i -H "Content-Type:application/json" -X Post -d "{\"Patients_Name\":\"Florence Kelly\",\"Patients_Doctor\":\"Doctor Smith\",\"Patients_Address\":\"High Street, Dublin\",\"Patients_Age\":19}" http://127.0.0.1:5000/patients
@app.route('/patients', methods=['POST'])
def create():
	global nextId
	if not request.json:
		abort(400)
	if not 'Patients_Name' in request.json:
		abort(400)
	patient = {
		"id": nextId,
		"Patients_Name": request.json['Patients_Name'],
		"Patients_Doctor": request.json['Patients_Doctor'],
		"Patients_Address": request.json['Patients_Address'],
		"Patients_Age": request.json['Patients_Age'],
	}
	nextId += 1
	patients.append(patient)
	return jsonify(patient)


#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Patients_Name\":\"Florence Welsh\",\"Patients_Doctor\":\"Doctor Smith\",\"Patients_Address\":\"High Street, Dublin\",\"Patients_Age\":20}" http://127.0.0.1:5000/patients/4
@app.route('/patients/<int:id>', methods=['PUT'])
def update(id):
	foundPatients = list(filter(lambda p: p['id']==id, patients))
	if (len(foundPatients) ==0):
		abort(404)
	foundPatients = foundPatients[0]
	if not request.json:
		abort(400)
	reqJson = request.json
	if 'Patients_Name' in reqJson:
		foundPatients['Patients_Name'] = reqJson['Patients_Name']
	if 'Patients_Name' in reqJson:
		foundPatients['Patients_Doctor'] = reqJson['Patients_Doctor']
	if 'Patients_Name' in reqJson:
		foundPatients['Patients_Address'] = reqJson['Patients_Address']
	if 'Patients_Age' in reqJson:
		foundPatients['Patients_Age'] = reqJson['Patients_Age']		
	return jsonify(foundPatients)
	

#curl -X DELETE "http://127.0.0.1:5000/patients/1"
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete(id):
	foundPatients = list(filter(lambda p: p['id']==id, patients))
	if (len(foundPatients) ==0):
		abort(404)
	patients.remove(foundPatients[0])
	return jsonify({"Deletion Completed": True})



 
if __name__ == '__main__' :
 app.run(debug= True)
