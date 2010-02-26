import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import mail

class Mailer(webapp.RequestHandler):
    def post(self):
        messageBody = self.request.get('content')
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, this webapp World! -- ')
        
        reqPath = self.request.path
        if reqPath == "/mail/send":
            self.sendmail(messageBody)

    # def get(self):
    #     self.response.headers['Content-Type'] = 'text/plain'
    #     self.response.out.write('Hello, this webapp World! -- ')
        
    #     reqPath = self.request.path
    #     if reqPath == "/mail/send":
    #         self.sendmail()

    def sendmail(self, messageBody):
        message = mail.EmailMessage(sender="Emre Sevinc <emre.sevinc@gmail.com>",
                            subject="Your account has been approved")

        message.to = "emre.sevinc@gmail.com"
        message.body = messageBody
        # message.body = """
        #  Dear Albert:

        #  Your example.com account has been approved.  You can now visit
        #  http://www.example.com/ and sign in using your Google Account to
        #  access new features.

        #  Please let us know if you have any questions.

        #  The example.com Team
        #  """
        message.send()

