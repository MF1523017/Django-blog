from django.conf.urls import url,include
from . import views
urlpatterns = [
	url(r'^$',views.archive),
	url(r'^create/',views.create_blogpost),
   ]