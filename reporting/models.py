from django.db import models
from picklefield import PickledObjectField

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


class GrandProfitAbilityReport(models.Model):
    created = models.DateTimeField(auto_now=True)
    created_for = models.DateField()
    data = PickledObjectField(default=dict)
    type = models.IntegerField(default=0, null=False)
    from_server = models.IntegerField(default=0, null=False)
    from_id = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f'{self.from_server},{self.from_id},{self.created},{self.created_for},{self.type}'


class SitesOnServers(models.Model):
    domain = models.CharField('domain name', max_length=100, unique=True)
    name = models.CharField('display name', max_length=50)
    from_server = models.IntegerField(default=0, null=False)
    from_id = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f'{self.from_server},{self.from_id},{self.domain},{self.name}'

    class Meta:
        # db_table = 'django_site'
        verbose_name = 'site'
        verbose_name_plural = 'sites'
        ordering = ('domain',)
