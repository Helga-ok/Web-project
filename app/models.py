from app import db
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

class Faculty(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	faculty_name = db.Column(db.String(64), index = True, unique = True)
	
	def __repr__(self):
		return '<Faculty %r>' % (self.faculty_name)

class Group(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
	group_name = db.Column(db.String(16), index = True)
	grouo_sum = db.Column(db.Integer)
	
	def __repr__(self):
		return '<Group %r>' % (self.group_name)

class Subject(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	subject_name = db.Column(db.String(64))

	def __repr__(self):
		return '<Subject %r>' % (self.subject_name)

class Lesson(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	start = db.Column(db.Time)
	end = db.Column(db.Time)


class Week(db.Model):
	day_id = db.Column(db.Integer, primary_key = True)
	day_name = db.Column(db.String(16))

	def __repr__(self):
		return '<Day %r>' %r (self.day_name)

class Schedule(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	day_of_week = db.Column(db.Integer, db.ForeignKey('week.day_id'))
	subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
	lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'))


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	group_name = db.Column(db.String(16))
	username = db.Column(db.String(64), index = True, unique = True)
	password_hash = db.Column(db.String(128))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	#def __init__(self, username, password, role):
	#	self.username = username
	#	password_hash = set_password(self, password)
	#	self.role = role

	
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def is_authenticated(self):
        	return True
 
    	def is_active(self):
        	return True
 
    	def is_anonymous(self):
        	return False
 
    	def get_id(self):
        	return unicode(self.id)

	def __repr__(self):
        	return '<User %r>' % (self.username)

