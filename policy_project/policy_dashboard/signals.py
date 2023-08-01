# signals.py

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Policy
from policy_project.settings import DEFAULT_FROM_EMAIL

@receiver(post_save, sender=Policy)
def send_policy_issued_email(sender, instance, created, **kwargs):
    if created and instance.policy_status == 'Policy Issued':
        subject = 'Your Policy Has Been Issued'
        message = f'Hello {instance.customer_name},\n\nYour policy with application number {instance.application_number} has been issued. Congratulations!\n\nThank you for choosing our services.\n\nRegards,\nYour Insurance Company'
        recipient_list = [instance.email]
        send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)
