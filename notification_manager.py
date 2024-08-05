import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_whatsapp(self, message_body):
        try:
            message = self.client.messages.create(
                from_=f"whatsapp:{os.environ['TWILIO_VERIFIED_NUMBER']}",
                body=message_body,
                to=f"whatsapp:{os.environ['TWILIO_WHATSAPP_NUMBER']}"
            )
            print(f"Message sent successfully: {message.sid}")
        except Exception as e:
            print(f"Failed to send message: {e}")