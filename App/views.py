from App import dataApp, db
from flask import render_template, request, redirect, session
from models import adminUsers, sensorData
from functools import wraps


# create decorator to ensure only logged in 
# personal can view data
def login_required(func):
	@wraps(func)
	def loginCheck(*args,**kwargs):
		if 'logged_in' in session:
			return func(*args,**kwargs)
		else:
			return redirect('/login')
	return loginCheck


@dataApp.route('/')
def home():
	return render_template('home.html')
	

@dataApp.route('/login', methods=["GET","POST"])
def loginPage():
	#check that person logging in has the permission to view data
	error = None
	try:
		if request.method == "POST":
			enteredUserName = request.form['userName']
			enteredPassword = request.form['password']
			check = db.session.query(adminUsers).all()
			for user in check:
				#print "database: ",user.userName, "keyedIn", enteredUserName 
				#print "database: ",user.password, "keyedIn", enteredPassword
				if user.userName == enteredUserName and user.password == enteredPassword:
					session['logged_in']=True
					#print session['logged_in']
					return redirect('/data')
			error = "invalid credentials"
			session.pop('logged_in',None)
		return render_template('login.html',
								error=error)
	except:
		return redirect('/')

@dataApp.route('/logout', methods=['GET','POST'])
@login_required
def logoutPage():
	print request.data
	if request.method == 'GET':
		session.pop('logged_in',None)
	return render_template("logout.html")

@dataApp.route('/data', methods=['GET', 'POST'])
@login_required
def dataPage():
	data = db.session.query(sensorData).all()
	if request.method == "POST":
		return redirect('/logout')
	return render_template("data.html",
							data = data)




