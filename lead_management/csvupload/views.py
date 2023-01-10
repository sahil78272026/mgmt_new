from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import *
import pandas as pd
from django.conf import settings
import os
import csv
from datetime import datetime

def home(request):
    if request.method=='POST':
        file2 = request.FILES['file']
        document = FileUpload.objects.create(file=file2)
        document.save()
        path = os.path.join(settings.BASE_DIR,'media') + '\\' + str(file2)
        df = pd.read_csv(path)
        now = datetime.now()
        current_time = now.strftime("%H")
        print(df.to_dict(orient='records'))
        df_to_dict = df.to_dict(orient='records')
        print(df_to_dict[1]['Name'])
        if int(current_time) >=9 and int(current_time) <18:
            return render(request,'index2.html',{'data': df.to_dict(orient='records')})
        else:
            return HttpResponse("Please add data between 9 to 6 only")
    return render(request,'index.html')

