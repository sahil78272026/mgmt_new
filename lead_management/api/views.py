from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from django.conf import settings
import os
from datetime import datetime
from .models import *

class CSVUploadView(APIView):
    def post(self, request):
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
            if int(current_time) >= 5 and int(current_time) < 19:
                return Response({'data': df_to_dict})
            else:
                return Response({'error': 'Please add data between 9 to 6 only'})
        return Response('index.html')