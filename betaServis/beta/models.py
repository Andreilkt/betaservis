from ipaddress import ip_address

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Betaservis(models.Model):
    main = models.TextField()
    services = models.TextField()
    works = models.TextField()
    forms = models.TextField()
    contacts = models.TextField()
    site = models.TextField()
    outsorcing = models.TextField()
    our_friends = models.TextField(default='test')



def __str__(self):
    return f"{self.main}, {self.services}, {self.works}, {self.forms}, {self.contacts}, {self.site}, {self.outsorcing} , {self.our_friends}"

class BetaservisText(models.Model):
    main_text = models.TextField()
    services_text = models.TextField()
    works_text = models.TextField()
    forms_text = models.TextField()
    contacts_text = models.TextField()
    site_text = models.TextField()
    outsorcing_text = models.TextField()
    our_friends_text = models.TextField(default='test')
    Betaservis = models.OneToOneField(Betaservis, on_delete=models.CASCADE, primary_key=True)

def __str__(self):
    return f"{self.main_text}, {self.services_text}, {self.works_text}, {self.forms_text}, {self.contacts_text}, {self.site_text}, {self.outsorcing_text}, {self.our_friends_text}"



class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема вопроса')
    email = models.EmailField(max_length=255 , verbose_name='Ваша почта')
    content = models.TextField(verbose_name='Ваш вопрос')
    Time_create = models.DateTimeField(auto_now_add=True, verbose_name='Когда отправили')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя',  blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='Гость', on_delete=models.CASCADE, null=True, blank=True)

    class meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']
        db_table = 'app_feedback'

    def __srt__(self):
        return f'Письмо от {self.email}'




