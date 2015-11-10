from App import db


class adminUsers(db.Model):

	__tablename__ = "ListOfAdminUsers"

	id = db.Column(db.Integer, primary_key=True)
	userName = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, userName, password):
		self.userName = userName
		self.password = password

	def __repr__(self):
		return "<{}>".format(self.userName)

class sensorData(db.Model):

	__tablename__ = "sensordatalog"

	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Integer,nullable=False)

	def __init__(self, val):
		self.value = val

	def __repr__(self):
		return "temperature sensor {}".format(self.val)