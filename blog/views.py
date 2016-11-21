from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.models import BlogPost,BlogPostForm

# Create your views here.
def archive(request):
	#post=BlogPost(title='mocktitle',body='mockbody',
	#	timestamp=datetime.now())
	posts=BlogPost.objects.all()[:10]
	#t=loader.get_template("archive.html")
	#c=Context({'posts':posts})
	#return HttpResponse(t.render(c))
	return render(request,"archive.html",{'posts':posts,'form':BlogPostForm()})
	#return render_to_response('archive.html',{'posts':posts},RequestContext(request))

def _saveBody(body):
	with open("body.cpp",'w') as bd:
		bd.write(body)
		bd.write(r"\nover")
def _readBody(bodyFile):
	with open(bodyFile,'r') as bd:
		text=bd.read()
	return text
def create_blogpost(request):
	if request.method=='POST':
		form=BlogPostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.timestamp=datetime.now()
			_saveBody(post.body)
			post.body=_readBody("body.cpp")
			post.save()

		return HttpResponseRedirect('/blog/')