from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    class Meta:
        db_table = "User"

class Post(models.Model):
    user = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

    class Meta:
        db_table = "Post"

class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50)

    class Meta:
        db_table = "Product"

class Login(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)

    class Meta:
        db_table = "Login"