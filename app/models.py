from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=300)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default=True, null=False)
    def __str__(self):
        return self.name

class Product (models.Model):
    Product_id = models.AutoField
    image = models.ImageField(upload_to="")
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default=True, null=False)
    Sub_Category= models.ForeignKey(Sub_Category, on_delete=models.CASCADE,default=True, null=False)
    name = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    detail = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")



class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

