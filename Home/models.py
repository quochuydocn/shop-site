from django.db import models

# Create your models here.
class Sanpham(models.Model):
    id = models.AutoField(primary_key=True)
    Code = models.CharField(max_length = 12, blank = True, null = True)
    Name = models.CharField(max_length=100, blank = True, null = True)
    ShowImg = models.FileField(upload_to = "./ShowImg", blank = True, null = True)
    Describe = models.TextField(blank = True, null = True)
    DescribeImg = models.FileField(upload_to = "./DescribeImg", blank = True, null = True)
    Useway   = models.TextField(blank = True, null = True)
    UsingImg = models.FileField(upload_to = "./UsewayImg", blank = True, null = True)
    Quantity = models.IntegerField(default = 0)
    Price  = models.IntegerField(default = 0)
    SalePrice = models.IntegerField(default = 0)
    BuyQuantity = models.IntegerField(default = 0)
    def __str__(self):
        return self.Name
