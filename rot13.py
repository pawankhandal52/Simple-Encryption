import os
import webapp2
import jinja2

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


app = webapp2.WSGIApplication([('/',MainPageHandler),
                              ],
                              debug=True)		