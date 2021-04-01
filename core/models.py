from django.db import models
from twilio.rest import Client
import os

class Core(models.Model):

    result=models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self,*args, **kwargs):
        if self.result<70:
            account_sid = 'AC58f02d80fa415fc0b1c6ba35035b06d1'
            auth_token = 'e8c96f185a92565ed1b8294a4a794bae'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body='Hi There !',
                                        from_='+18328502576',
                                        to='+919080483660',
                                        )

            print(message.sid)
        return super().save(*args, **kwargs)
                        
            
        