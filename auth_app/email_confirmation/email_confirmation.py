from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.authtoken.models import Token

"""
Sends the confirmation email after registering.
The user has to click on the link containing the Token, to confirm the registered email address.
"""
def send_confirmation_email(user):
    token, created = Token.objects.get_or_create(user=user)
    confirmation_link = f"http://127.0.0.1:8000/videoflix/auth/confirm/{token.key}/"
    html_message = render_to_string('email_confirmation.html', {
        'username': user.username,
        'confirmation_link': confirmation_link
    })
    plain_message = strip_tags(html_message)

    email = EmailMultiAlternatives(
        subject="Videoflix - Confirm your email address",
        body=plain_message,
        from_email='noreply@videoflix.peeet.net',
        to=[user.email]
    )
    email.attach_alternative(html_message, 'text/html')

    with open('media/img/logo_full.png', 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-ID', '<logo>')
        img.add_header('Content-Disposition', 'inline', filename='logo.png') 
        email.attach(img)

    email.send()