from django.db import models


from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

def validate_image_dimensions(image):
    image = Image.open(image)
    min_width = 1000
    min_height = 1000
    if image.width < min_width or image.height < min_height:
        raise ValidationError(f"The image must be at least {min_width}x{min_height} pixels.")




class PageBase(models.Model):
    title=models.CharField(max_length=50)
    sub_title=models.CharField(max_length=50)
    
    bg_image=models.ImageField(upload_to='images/%Y/%m/%d',validators=[validate_image_dimensions])

    created_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

        def __str__(self):
            return self.title
        

class HomePage(PageBase):
    pass

class AboutPage(PageBase):
    description = models.TextField(blank=True)
    
class ContactPage(PageBase):
    description=models.TextField()

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT=('DF','Draft')
        PUBLISHED=('PB','Published')
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    bg_image=models.ImageField(upload_to='images/%Y/%m/%d/background_image')
    post_image=models.ImageField(upload_to='images/%Y/%m/%d/post_image')
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)


    class Meta:
        ordering=['-publish']

        indexes=[
            models.Index(fields=['-publish'])
        ]
 
    def __str__(self):
        return self.title
    