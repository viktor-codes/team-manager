from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup
from django.utils.translation import ugettext_lazy as _


class MyAccountAdapter(DefaultAccountAdapter):
    def is_email_verified(self, email_address):
        # Automatically consider email verified for social account users
        if email_address.provider in ["facebook", "google"]:
            return True
        return super().is_email_verified(email_address)

    def send_confirmation_mail(self, request, emailaddress, signup):
        # Do not send confirmation email if the user is signing up via social accounts
        if emailaddress.provider in ["facebook", "google"]:
            return  # Skip sending confirmation email
        return super().send_confirmation_mail(request, emailaddress, signup)
