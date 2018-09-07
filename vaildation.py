import re

username =  "^[a-zA-Z0-9_-]{3,20}$"
password = "^.{3,20}$"
email    = "^[\S]+@[\S]+.[\S]+$"


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
  
def valid_username(username):
  return USER_RE.match(username)


def vaild_email(email):
  return EMAIL_RE.match(email)

def vaild_password(password):
	return PASSWORD_RE.match(password)

def isPasswordSame(password,verify):
	if 	password == verify:
		return True
	else:
		return False	