from requests.auth import HTTPBasicAuth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render
from rest_framework.utils import json
import boto3
import re
import os
import pathlib
from io import StringIO
import pandas as pd
from django.http import HttpResponseNotFound, JsonResponse
# Create your views here.
from django.http import HttpResponse


@api_view(['GET'])

def objectsList(request):
	s3=boto3.resource('s3',aws_access_key_id="AKIAZ3M27WFM7RONFHXU",aws_secret_access_key="Q9Xm2basNJYLXHWtT0AaIHBo+tPmZU4YaQDfgxxt")
	bucket = s3.Bucket('backend-dev-test')
	objectsList=[]
	for my_bucket_object in bucket.objects.all():
		objectsList.append(my_bucket_object.key)
	
	return Response(objectsList)

@api_view(['GET'])
def downloadObject(request):
	response=""

	fileName = request.GET.get('fileName')
	print(fileName)
	s3=boto3.client('s3',aws_access_key_id="AKIAZ3M27WFM7RONFHXU",aws_secret_access_key="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")
	try:
		s3.download_file('backend-dev-test',fileName, fileName)
		response="success"
	except:
		response="file not found"
	return  Response(response)

@api_view(['POST'])
def uploadObject(request):
	data = request.body.decode('utf-8')
	body = json.loads(data)
	fileDir = body['fileDir']
	saveAs = body['saveAs']

	s3=boto3.resource('s3',aws_access_key_id="AKIAZ3M27WFM7RONFHXU",aws_secret_access_key="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")
	bucket = s3.Bucket('backend-dev-test')

	try:
		bucket.upload_file(fileDir, saveAs)
		response="success"
	except FileNotFoundError:
		response="file not found, please check the file path"

	return  Response(response)


@api_view(['POST'])
def deleteObject(request):
	data = request.body.decode('utf-8')
	body = json.loads(data)
	fileName = body['fileName']
	response=""
	s3=boto3.resource('s3',aws_access_key_id="AKIAZ3M27WFM7RONFHXU",aws_secret_access_key="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")
	try:
		obj = s3.Object("backend-dev-test", fileName)
		obj.delete()
		response="OK"
	except:
		response="Error"

	return  HttpResponse(response)
	
@api_view(['GET'])
def readCsvObject(request):

	fileName = request.GET.get('fileName')
	s3=boto3.client('s3',aws_access_key_id="AKIAZ3M27WFM7RONFHXU",aws_secret_access_key="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")
	bucket_name = 'backend-dev-test'
	object_key = 'acramentorealestatetransactions.csv'
	csv_obj = s3.get_object(Bucket=bucket_name, Key=fileName)
	body = csv_obj['Body']
	csv_string = body.read().decode('utf-8')
	df = pd.read_csv(StringIO(csv_string))

	return HttpResponse(df.to_html())
