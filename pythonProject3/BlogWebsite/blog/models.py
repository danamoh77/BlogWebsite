from django.db import models



class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.username
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
      post = models.CharField(max_length=300)
      user = models.CharField(max_length=300)
      content = models.TextField()
      date_posted = models.DateTimeField(auto_now_add=True)

      def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'