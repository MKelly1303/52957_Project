#!flask/bin/python
from flask import Flask


app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/')
def index():
 return"Hello, World!"
 
@app.route('/book/<int:id>')
def getBook(id):
	return"You want book with id of "+ str(id)
 
if __name__ == '__main__' :
 app.run(debug= True)
