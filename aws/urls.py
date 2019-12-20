from django.urls import path

from . import views


app_name = 'aws'

urlpatterns = [
	path('objectsList', views.objectsList, name='objectsList'),
	path('downloadObject', views.downloadObject, name='downloadObject'),
	path('uploadObject', views.uploadObject, name='uploadObject'),
	path('deleteObject', views.deleteObject, name='deleteObject'),
	path('readCsvObject', views.readCsvObject, name='deleteObject'),
	
]