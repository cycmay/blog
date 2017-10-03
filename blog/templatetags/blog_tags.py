from django import template
from ..models import Post,Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num = 5):
	return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
	return Post.objects.dates('create_time','month',order = 'DESC')
	#order = 'DESC' 表示降序排列 ，month是精度

@register.simple_tag
def get_categories():
	return Category.objects.all()