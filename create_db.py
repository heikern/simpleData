from App import db
from App.models import adminUsers

db.create_all()

db.session.add(adminUsers("heikern","admin"))
db.session.add(adminUsers("heimern","admin"))
db.session.add(adminUsers("siewhong","admin"))
db.session.add(adminUsers("yokewah","admin"))

db.session.commit()