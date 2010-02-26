import urllib

# url = "http://localhost:8081/mail/send"
url = "http://clozefox.appspot.com/mail/send"

data = {  'msgRecipient' : 'emre.sevinc@gmail.com'
         ,'msgSubject'   : 'Test subject'
         ,'msgBody'      : 'Test body'
          }

urldata = urllib.urlencode(data)
results = urllib.urlopen(url, urldata).read()

print results
