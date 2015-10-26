from App import db
from App.models import sensorData, adminUsers


db.session.add(adminUsers("tom","admin"))
db.session.add(adminUsers("marry","admin"))
db.session.add(adminUsers("james","admin"))
db.session.add(adminUsers("jane","admin"))

db.session.add(sensorData(6))
db.session.add(sensorData(7))
db.session.add(sensorData(8))
db.session.add(sensorData(12))
db.session.add(sensorData(42))

db.session.commit()