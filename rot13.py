import os
import webapp2
import jinja2
import vaildation

template_dir = os.path.join(os.path.dirname(__file__),'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)

	def render_str(self,template,**prams):
		t = jinja_env.get_template(template)
		return t.render(prams)

	def render(self,template,**kw):
		self.write(self.render_str(template, **kw))


class MainPageHandler(Handler):
	def get(self):
		self.render("form.html")    

	def post(self):
		text = self.request.get("text")
		output_text = ""
		#first get the charcter using iter
		for char in text:
			
			#Now first chcek char is alphbate or not
			ascii_value = ord(char)
			if ascii_value in range(65,91):
				change_value =  ascii_value + 13
				if change_value  not in range(65,91):
					remain = change_value - 91
					#print(chr(65+remain))
					output_text += chr(65+remain)
				else:
					#print(chr(change_value))
					output_text += chr(change_value)		
			elif ord(char) in range(97,123):
				 change_value =  ascii_value + 13
				 if change_value  not in range(97,123):
					remain = change_value - 123
					#print(chr(97+remain))
					output_text += chr(97+remain)
				 else:
					#print(chr(change_value))
					output_text += chr(change_value)
			else:
				#print("No")
				output_text += char	
		self.render("form.html",text = output_text)    		


class SignupPageHandler(Handler):
	def get(self):
		self.write_form()
	def post(self):
		user_name = self.request.get("username")	
		password = self.request.get("password")	
		verify = self.request.get("verify")
		email = self.request.get("email")
		print(vaildation.valid_username(user_name))
		print(vaildation.vaild_password(password))
		print(vaildation.vaild_email(email))
		print(vaildation.isPasswordSame(password,verify))
		username_error = ""
		password_error = ""
		verified_password_error = ""
		email_error = ""
		is_all_vaild = False
		if not vaildation.valid_username(user_name):
			is_all_vaild = True
			username_error = "Invaild User name"
			
		if not vaildation.vaild_password(password):
			is_all_vaild = True
			password_error = "Password is  Invaild"
		if not vaildation.isPasswordSame(password,verify):
			is_all_vaild = True
			verified_password_error = "Password is not same"

		if len(email)!=0:
			if not vaildation.vaild_email(email):
				is_all_vaild = True
				email_error = "Please fill vaild Email"

		if is_all_vaild	:
			self.write_form(username_error,password_error,verified_password_error,email_error,user_name,email)
		else:
			self.redirect("/welcome?username=%s"%user_name)	


	def write_form(self,username_error= "",password_error = "",verified_password_error= "",email_error = "",username="",password="",verify="",email=""):
		post_data = SignUpData(username_error,password_error,verified_password_error,email_error,username,password,verify,email)
		self.render("signup_form.html",data = post_data)

class SignUpData:
	def __init__(self,username_error,password_error,verified_password_error,email_error,username,password,verify,email):
		self.username_error = username_error
		self.password_error = password_error
		self.verified_password_error = verified_password_error
		self.email_error = email_error
		self.username = username
		self.password = password
		self.verify = verify
		self.email = email

class WelcomePage(Handler):
	def get(self):
		self.render("welcome.html",welcome = self.request.get("username"))
		

app = webapp2.WSGIApplication([('/',MainPageHandler),
                              	('/signup',SignupPageHandler),
                              	('/welcome',WelcomePage)],
                              debug=True)		