from django.db import models
from users.models import User




class Tag(models.Model):
    tag = models.CharField(max_length=150)

    def __str__(self):
        return self.tag


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='pic_or_video')
    published_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return f'{self.user} comment for {self.post}'

# class PostPictureOrVideo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')
#     pic_or_video = models.FileField(upload_to='pic_or_video')
    
#     def __str__(self):
#         return self.post

