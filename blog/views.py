from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.models import BlogPost,BlogPostForm

cppPath='/home/lipei/learn/Django/Django-blog/'
# Create your views here.
def archive(request):
	#post=BlogPost(title='mocktitle',body='mockbody',
	#	timestamp=datetime.now())
	posts=BlogPost.objects.all()[:1]
	#t=loader.get_template("archive.html")
	#c=Context({'posts':posts})
	#return HttpResponse(t.render(c))
	return render(request,"archive.html",{'posts':posts,'form':BlogPostForm()})
	#return render_to_response('archive.html',{'posts':posts},RequestContext(request))
def _computeResult(f):
	import re
        result=list()
        with open(f,'r') as rs:
            for r in rs:
                try:
                    score=[int(num) for num in re.findall(r'[0-9]+',r) if 0<int(num)<=100]
                    result.append(max(score))
                except:
                    result.append(60)
        if result==[]:
            return 60
        else:
            return max(result)
def _saveBody(body):
	with open("{}body.cpp".format(cppPath),'w') as bd:
		bd.write(body)
#		bd.write(r"\nover")
def _compileCpp():
	import os
	if os.path.exists('{0}result.txt'.format(cppPath)):
		os.remove('{0}result.txt'.format(cppPath))
	if os.path.exists('{0}result'.format(cppPath)):
		os.remove('{0}result'.format(cppPath))
	os.system('g++ -o {0}result {0}body.cpp'.format(cppPath))
	os.system('{0}result > {0}result.txt'.format(cppPath))
def _readBody(bodyFile):
	with open(bodyFile,'r') as bd:
		text=bd.read()
	return text
def create_blogpost(request):
	if request.method=='POST':
		form=BlogPostForm(request.POST)
		#form=BlogPostForm(initial={'title':'1'}
		if form.is_valid():
			post=form.save(commit=False)
			post.timestamp=datetime.now()
			_saveBody(post.body)
                        _compileCpp()
			result=_computeResult("{}result.txt".format(cppPath))
			post.body="your score is "+str(result)
			post.save()

		return HttpResponseRedirect('/blog/')

if __name__=='__main__':
	cppPath='/home/lipei/learn/Django/Django-blog/'
	print _computeResult("{}result.txt".format(cppPath))
