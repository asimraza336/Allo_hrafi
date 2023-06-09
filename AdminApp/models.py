from django.db import models
# from Users import User

class City(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    city_image = models.FileField(upload_to="cities/", null=True, blank=True, default="Profile_Pictures/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300)
    category_icon = models.FileField(upload_to="categories_icon/", null=True, blank=True, default="Profile_Pictures/default.png")
    category_image = models.FileField(upload_to="categories/", null=True, blank=True, default="Profile_Pictures/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Service(models.Model):

    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300)
    thumbnail_image = models.FileField(upload_to="service_thumbnail/")
    provider_user = models.OneToOneField('Users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class ServiceImage(models.Model):
    
    image = models.FileField(upload_to="service_images/")
    service = models.ForeignKey(Service, related_name='service', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return self.name