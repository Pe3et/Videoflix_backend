from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.authtoken.models import Token

"""
Sends the confirmation email after registering.
The user has to click on the link containing the Token, to confirm the registered email address.
"""
def send_confirmation_email(user):
    token, created = Token.objects.get_or_create(user=user)
    print(token)
    confirmation_link = f"https://videoflix.peeet.net/confirm/{token.key}/"
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
    email.send()