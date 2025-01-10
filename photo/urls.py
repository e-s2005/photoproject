from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
	path('',views.IndexView.as_view(), name='index'),
	# path('photo-detail/<int:pk>',
	# views.Detailview.as_view(),
	# name='photo_detail'),
] 
