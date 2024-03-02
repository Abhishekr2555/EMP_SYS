from django.conf import settings
from twilio.rest import Client
import random


class messhanlder:
    phone_num = None
    otp = None

    def __int__(self, phone_num, otp) -> None:
        self.phone_num = phone_num
        self.otp = otp

    def send_otp(self):
        client = Client(settings.ACCOUNT_SID,settings.AUTH)
        
        message = client.messages.create(
        to="123",
        from_="456",
        body="Your OTP is {self.otp}")

