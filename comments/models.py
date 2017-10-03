from django.db import models

# Create your models here.
class Comment(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 255)
	url = models.URLField(blank = True)
	text = models.TextField()
	create_time = models.DateTimeField(auto_now_add = True)
	#auto_now_add 当评论保存到数据库中时，自动把create_time的值指定为当前时间
	post = models.ForeignKey('blog.Post') #这个评论关联到谋篇文章的Post
	def __str__(self):
		return self.text[:20]