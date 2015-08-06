from views import db 
from models import Task
from datetime import date

#create db and db table
db.create_all()

#insert data
# db.session.add(Task("Finish this project", date(2015, 8, 15), 7, 1))
# db.session.add(Task("Start new project", date(2015, 8, 17), 4, 1))

#commit changes
db.session.commit()
