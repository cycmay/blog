# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	'''
	Django 要求模型必须继承model.Model类
	category 只需要一个简单的分类名name就可以了
	CharField 指定了分类名name的数据类型，CharField是字符型
	CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
	当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等
	'''
	name = models.CharField(max_length = 100)

#文章post，分类category，标签tag

class Tag(models.Model):
	'''
	标签Tag比较简单，继承Category类
	'''
	name = models.CharField(max_length = 100)

class Post(models.Model):
	'''
	文章的数据库表稍微复杂一些，主要是涉及字段更多
	'''
	#文章标题
	title = models.CharField(max_length = 70)

	#文章正文，使用了TextField
	#存储比较短的字符串，我们可以使用CharField，但是文章通常是一大段字符
	body = models.TextField()

	#文章的创建时间，最后一次修改时间，存储时间的字段用DateTimeField类型
	create_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	#文章摘要，可以没有，但是默认情况CharField要求我们必须存入数据，否则就会报错
	#指定CharField的blank=True 参数值后就可以允许空值了
	excerpt = models.CharField(max_length = 200,blank = True)
	#一个分类下有多个文章使用ForeignKey,一对多的关联关系
	#一篇文章有多个标签，一个标签也可能有多篇文章，使用ManyToManyField,表明这是多对多的关系
	#文章也可以没有标签，tags指定blank=True

	category = models.ForeignKey(Category)
	Tags = models.ManyToManyField(Tag,blank = True)

	#文章作者
	# 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
	author = models.ForeignKey(User)

	def get_absolute_url(self):
		return reverse('blog:detail',kwargs = {'pk' : self.pk})

	class Meta:
		ordering = ['-create_time']