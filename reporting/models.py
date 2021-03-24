from django.db import models

# Create your models here.


class Uniquelid(models.Model):
    ''' Unique LIDs report '''
    email = models.EmailField('E-mail', max_length=254, default='')
    phone = models.CharField('Phone Number', max_length=250, default='')
    site = models.TextField('Site')
    state = models.TextField('State')
    join_date = models.DateTimeField('Дата публикации')
    sale_person = models.TextField('Sales person')

    def __str__(self):
        # return self.email, self.phone, self.site, self.state, self.join_date, self.sale_person
        return f'{self.email}, {self.phone}, {self.site}, {self.state}, {self.join_date}, {self.sale_person}'
        # return self.email

    class Meta:
        verbose_name = 'Unique LID'
        verbose_name_plural = 'Unique LIDs'
