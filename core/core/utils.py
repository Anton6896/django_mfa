from twilio.rest import Client
from django.conf import settings


def twilio_send_sms(message: str, phone_number: str):
    client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)

    message = client.messages.create(
        body=message,
        from_=settings.TWILIO_NUMBER,
        to=phone_number
    )

    return message.sid
