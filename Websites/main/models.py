from django.db import models
from django.urls import reverse

Gender_Choice= [
    ('male', 'Male'),
    ('female', 'Female'),
        ]
class Signup(models.Model):
    name = models.CharField(max_length=250)
    login = models.CharField(max_length=250, default='')
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    birthdate = models.DateTimeField()
    gender = models.CharField(choices=Gender_Choice, max_length=128,default='')
    password = models.CharField(max_length=250, default=0)


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})

class Posts(models.Model):
    title=models.CharField(max_length=255, verbose_name="Taqyryp")
    is_published=models.BooleanField(default = True, verbose_name="Shygarylym")
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})
    def myage(self):
        return 18


class Comment(models.Model):
    nickname = models.CharField('Author', max_length=50)
    comment = models.TextField('Comment', max_length=300)

    def __str__(self):
        return f'{self.nickname} {self.id}'


    class Meta:
        verbose_name="Пікір"
        verbose_name_plural="Пікірлер"
        ordering=['-nickname','comment']
class Basket(models.Model):
    trips = models.CharField('Trips', max_length=50, default='')
    prices = models.CharField('Prices', max_length=50, default='')
    description = models.TextField('Description', max_length= 200, default='')
    def __str__(self):
        return self.trips

class Hotel(models.Model):
    name = models.CharField('Hotel name', max_length=50)
    descrip = models.TextField('Hotel description', max_length=200)

    def __str__(self):
        return self.name
