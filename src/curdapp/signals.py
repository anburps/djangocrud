
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib import messages
from django.conf import settings
from curdapp.models import CrudView


@receiver(pre_save, sender=CrudView)
def send_email_on_save(sender, instance, **kwargs):
    
    subject = 'Test Email'
    message = 'This is a test email sent using SMTP in Django.'
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = ['aanburpskn@gmail.com']
    
    send_mail(subject, message, from_email, recipient_list)
    
    print("pre save works")
    

