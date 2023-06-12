from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Walk_In
from django.core.mail import send_mail


@receiver(post_save, sender=Walk_In)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        send_mail("Walkin Details", instance.walk_in_datetime, "test@test.com", [instance.lead.email_id,instance.vendor.email_id],fail_silently=True)
        print("Emails sent to both vendor and visitor")