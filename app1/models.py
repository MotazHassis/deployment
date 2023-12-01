from django.db import models
import re
import bcrypt
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['fname']) < 2 :
            errors['first']= 'First name should be more than 5 characters'
        if len(postData['lname']) < 2 :
            errors['last']= 'Last name should be more than 5 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']= 'Invalid Email Address'
        if postData['password'] != postData['confirm']:
            errors['password']= 'Password not match'
        return errors


class User(models.Model):
    first = models.CharField(max_length=45)
    last = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password = models.TextField()
    objects= UserManager()
# Create your models here.
