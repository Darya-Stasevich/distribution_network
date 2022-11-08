import qrcode

from distribution_network.celery import app
from main.models import Element
from django.core.mail import EmailMessage


@app.task
def send_qrcode(title, email):
    elem = Element.objects.get(title=title)
    img = qrcode.make(elem.contact)
    img.save(f'media/{title}.png')
    em = EmailMessage(subject='Ловите qr-код!', body='New Qr code', to=[email])
    em.attach_file(f'media/{title}.png')
    em.send()