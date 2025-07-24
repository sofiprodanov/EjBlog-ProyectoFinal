from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import uuid
import os
    

class Category (models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='post')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    content =models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField(default=True)
    #para likes, estrellas, favoritos, se asocia a post
    
    def __str__(self):
        return self.titulo
    
    @property
    def amount_comments(self):
        return self.comments.count()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
    
    def gernerate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Post.objects.filter(slug=unique_slug).exists(): 
            unique_slug = f'{slug}-{num}'
            num += 1
    
        return unique_slug


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= 'comments')
    content =models.TextField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


def get_image_filename(instance, filename):
    post_id = instance.post.id
    images_count = instance.post.images.count()
    #miimagen.png
    #miimagen   .png
    _, file_extension = os.path.splitext(filename)
    new_filename = f'post_{post_id}_image_{images_count+1}{file_extension}'
    return os.path.join('post/cover/', new_filename)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_filename)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'PostImage {self.id}'