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
        msgRecipient = self.request.get('msgRecipient')
        msgSubject   = self.request.get('msgSubject')
        msgBody      = self.request.get('msgBody')
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Your mail has been sent!')
        
        reqPath = self.request.path

        if reqPath == "/mail/send":
            self.sendmail(msgRecipient, msgSubject, msgBody)


    def sendmail(self, msgRecipient, msgSubject, msgBody):
        if msgRecipient == "": # create a default recipient
            msgRecipient = "emre.sevinc@gmail.com"

        if msgSubject == "": #create a default subject
            msgSubject = "Default subject"

        if msgBody == "": # create a default message
            msgBody = "Default message body"


        message = mail.EmailMessage(sender  = "Emre Sevinc <emre.sevinc@gmail.com>",
                                    subject = msgSubject)

        message.to = msgRecipient
        message.body = msgBody

        message.send()

