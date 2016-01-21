from bottle import route, run, template,response, get, post,request, static_file
import os
from config import *
import staticFilesForAbout
import staticFilesForLogin
import staticFilesForApplication



@route('/')
def greet(name='Stranger'):
	print 'hello'
	print os.path.dirname(os.path.abspath(__file__))
	return static_file('index.html', root="/home/manchanda/Projects/SMARTHOME/html/ABOUT")


@get('/login')
def login_page(name='Stranger'):
	print 'hello'
	print os.path.dirname(os.path.abspath(__file__))
	return static_file('index.html', root="/home/manchanda/Projects/SMARTHOME/html/Login")


@post('/login') # or @route('/login', method='POST')
def login():
	username = request.forms.get('userID')
	password = request.forms.get('KEY')
	if(username == configs_user['username'] and password == configs_user['password']):
		return static_file('index.html', root="/home/manchanda/Projects/SMARTHOME/html/Application")

	else:
		return template("<p> Login unsuccessful {{name}} {{pass1}} </p>",name=username, pass1=password)


@route('/test')
def testing():
	print "hee"
	username=configs['username']+configs['password']
	return 'Hey'+username

@route('/lights')
def toggle():
	print "Hello Lights are toggle"
	return "toggle"



#Mobile ENDPOINTS

@get('/logintest') # or @route('/login')
def login():
	return '''
		<form action="/login" method="post">
           	Username: <input name="username" type="text" />
            	Password: <input name="password" type="password" />
            	<input value="Login" type="submit" />
        	</form>
   		'''


@post('/data') # or @route('/login', method='POST')
def data():
	data=getdata()
	return data

@post('/logincheck') # or @route('/login', method='POST')
def checklogin():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if(username == configs_user['username'] and password == configs_user['password']):
		return "1"

	else:
		return "0"



def getdata():
	return "Test data"


run(host='192.168.43.65', port=8080, debug=True)
