#Implement method overriding for a `Notification` class where `send()`
#  is overridden in `EmailNotification` and `SMSNotification`
from abc import ABC,abstractmethod
class Notification:
    def send(self):
        pass
class Sms_notification:
    def send(self):
        print("The sms have been sent...")
    
class Email_notification:
    def send(self):
        print("The Email notification is sent...")
def myfunction(obj):
    obj.send()
    
    
email=Email_notification()
sms=Sms_notification()
myfunction(email)
myfunction(sms)
