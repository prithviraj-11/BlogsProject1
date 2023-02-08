from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "UserInfo"

class BlogDetails(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pictures')
    creation_date = models.DateField()
    published_date = models.DateField(blank=False)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = "BlogDetails"