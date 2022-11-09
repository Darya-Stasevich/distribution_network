import random

import qrcode
from django.db.models import F

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


@app.task
def increase_debt():
    Element.objects.update(debt=F('debt') + random.randint(5, 500))


@app.task
def decrease_debt():
    Element.objects.update(debt=F('debt') - random.randint(100, 10_000))


@app.task
def clear_debt_async(id):
    Element.objects.filter(id=id).update(debt=0)
