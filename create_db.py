from App import db
from App.models import adminUsers

db.create_all()

db.session.add(adminUsers("tom","admin"))
db.session.add(adminUsers("marry","admin"))
db.session.add(adminUsers("james","admin"))
db.session.add(adminUsers("jane","admin"))

db.session.commit()