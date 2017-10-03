from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm
# Create your views here.

def post_comment(request,post_pk):
	#首先获取被评论的文章，使用404返回是与否
	post = get_object_or_404(Post,pk = post_pk)

	#HTTP 一般提交表单使用的是post请求
	if request.method == 'POST':
		#用户提交的数据存在request.POST 中，一个类字典对象
		form = CommentForm(request.POST)
		#调用form.is_valid()方法，django自动检查数据是否符合要求
		if form.is_valid():
			comment = form.save(commit = False)

			#关联到被评论的文章 
			comment.post = post
			#将评论存储到数据库中
			comment.save()
			#重新 定向post的详情页
			return redirect(post)
	else:
		#数据不合法，
		comment_lists = post.comment_set.all()
		context = {'post':post,
					'form':form,
					'comment_list':comment_list
					}
		return render(request,'blog/detail.html',context = context)
	return redirect(post)