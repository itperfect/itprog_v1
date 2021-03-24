from django.db import models

# Create your models here.


class Uniquelid(models.Model):
    ''' Unique LIDs report '''
    email = models.EmailField('E-mail', max_length=254, default='')
    phone = models.CharField('Phone Number', max_length=250, default='')
    site = models.TextField('Site')
    state = models.TextField('Site')
    join_date = models.DateTimeField('Дата публикации')
    sale_person = models.TextField('Site')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Unique LID'
        verbose_name_plural = 'Unique LIDs'
