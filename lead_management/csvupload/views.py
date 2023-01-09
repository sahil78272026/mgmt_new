from django.shortcuts import render
from .forms import CSVUploadForm
from django.http import HttpRequest,HttpResponse
from .models import *
import pandas as pd
from django.conf import settings
import os

import csv

def home(request):
    
    print('request.scheme : ' , request.scheme) # showing the type of protocol, is it http or https
  # print('request.body : ' ,request.body)
    print('request.POST : ' ,request.POST)
    print('request.path : ' ,request.path)
    print('request.content_type : ' ,request.content_type)

    if request.method=='POST':
        file2 = request.FILES['file']
        document = FileUpload.objects.create(file=file2)
        document.save()
        path = os.path.join(settings.BASE_DIR,'media') + '\\' + str(file2)
        df = pd.read_csv(path)
        return render(request,'index2.html',{'data': df.to_dict(orient='records')})
    return render(request,'index.html')