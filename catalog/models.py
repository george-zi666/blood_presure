from django.db import models

from django.urls import reverse  # To generate URLS by reversing URL patterns


class Measure(models.Model):
    title = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
   
    def get_absolute_url(self):
        return reverse('measure-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.title)




import uuid  
from datetime import date


class UsersMeasurement(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    measure = models.ForeignKey('Measure', on_delete=models.SET_NULL, null=True)
    systolic = models.IntegerField(max_length=10)
    dyastolic = models.IntegerField(max_length=10)
    pulse = models.IntegerField(max_length=10)
    date_measure = models.DateField(null=True, blank=True)

    def is_overdue(self):
        if self.date_measure and date.today() > self.date_measure:
            return True
        return False

    LOAN_STATUS = (
        ('p', 'выполено'),
        ('n', 'не выполнено'),
     )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='p',
        help_text='status measurement')

    class Meta:
        ordering = ['date_measure']

    def __str__(self):
       return '{0} ({1})'.format(self.user, self.measure.title)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_login = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
