from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils import timezone
from datetime import datetime

class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/")
    alt_text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text

# Category
class Project(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")
    active=models.BooleanField(default=False)
    starttime=models.DateTimeField()

    class Meta:
        verbose_name_plural='2. Projects'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    

# Brand
class Role(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='3. Roles'

    def __str__(self):
        return self.title




# Product Model
class Employee(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    Experience=models.TextField()
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    is_featured=models.BooleanField(default=False)


    class Meta:
        verbose_name_plural='4. Employees'

    def __str__(self):
        return self.title

# Product Attribute
class EmployeeAttribute(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product_imgs/",null=True)

    class Meta:
        verbose_name_plural='5. EmployeesAttributes'

    def __str__(self):
        return self.employee.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    