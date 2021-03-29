from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import City
from .serializers import CitySerializer,QHSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import pandas as pd
from .models import City,QH
from django.shortcuts import render
from django.db.models import Q
df = pd.read_csv('https://raw.githubusercontent.com/hoangphuc0611/darknet/master/canho2.csv') 
df_html = pd.read_csv('https://raw.githubusercontent.com/hoangphuc0611/darknet/master/filehtml.csv')




class CityAPIView(APIView):
    model = City
    # all_data =df.values.tolist()
    # for i in all_data:
    #     cre = City.objects.create(stt=str(i[0]),name=str(i[1]),price=str(i[2]),address=str(i[3]),ban_giao=str(i[4]),loai_hinh=str(i[5]),quy_mo=str(i[6]),so_tang=str(i[7]),dien_tich=str(i[8]),toa_do=str(i[9]),image=str(i[10]))
    def post(self, request):
        print(request.data)
        query = request.data['name']
        if not query :
            query = ""
        query1 = request.data['district']
        if not query1 :
            query1 = ""
        query2 = request.data['price']
        if not query2 :
            query2 = ""

        lis_gia= [i[2] for i in df.values.tolist()] 
        lis_price=[]
        if query2=='4':
            lis_price.append('Đang cập nhật')
        if query2=='1':
            for i in lis_gia:
                if i=='Đang cập nhật':
                    pass
                else:
                    # print(i)
                    x = int(i.split()[0].split('-')[0])
                    # print(x)
                    if x <= 80:
                        lis_price.append(i)
        if query2=='2':
            for i in lis_gia:
                if i=='Đang cập nhật':
                    pass
                else:
                    # print(i)
                    x = int(i.split()[0].split('-')[0])
                    y = int(i.split()[0].split('-')[1])
                    # print(x)
                    if x < 80 and y >= 130:
                        lis_price.append(i)
                    if x >= 80 and x <= 130:
                        lis_price.append(i)
        if query2=='3':
            for i in lis_gia:
                if i=='Đang cập nhật':
                    pass
                else:
                    # print(i)
                    x = int(i.split()[0].split('-')[0])
                    y = int(i.split()[0].split('-')[1])
                    # print(x)
                    if y >= 130:
                        lis_price.append(i)
        if len(lis_price)==0:
            lis_price=lis_gia

        # print(request.query_params['q'])
        citis = City.objects.filter(
            Q(name__icontains=query) & Q(address__icontains=query1) & Q(price__in=lis_price)
        )
        # citis = City.objects.all()
        serializer = CitySerializer(citis, many=True)
        all_data=serializer.data
        # print(all_data)
        return Response(all_data)


    # def post(self, request):
    #     serializer = CitySerializer(data =request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

          
class QHAPIView(APIView):
    model = QH
    all_data =df_html.values.tolist()
    def post(self, request):
        lis_name= [i[1] for i in df.values.tolist()]
        query = request.data['name']
        if not query :
            query = ""
        count=0
        for i in range(len(lis_name)):
            if lis_name[i]==query:
                count=i+1
                break
        query = "vitri"+str(count)+".html"
        qhs = QH.objects.filter(
            Q(stt=query)
        )
        serializer = QHSerializer(qhs,many=True)
        all_data=serializer.data
        print(all_data)
        return Response(all_data)
    # for i in all_data:
    #     cre = QH.objects.create(stt=str(i[0]),html=str(i[1]))
    
class HomePageView(TemplateView):
    template_name = 'search_results.html'


def vitri1(request):   
    return render(request, 'vitri1.html')
def vitri2(request):   
    return render(request, 'vitri2.html')
def vitri3(request):   
    return render(request, 'vitri3.html')
def vitri4(request):   
    return render(request, 'vitri4.html')
def vitri5(request):   
    return render(request, 'vitri5.html')
def vitri6(request):   
    return render(request, 'vitri6.html')
def vitri7(request):   
    return render(request, 'vitri7.html')
def vitri8(request):   
    return render(request, 'vitri8.html')
def vitri9(request):   
    return render(request, 'vitri9.html')
def vitri10(request):   
    return render(request, 'vitri10.html')
def vitri11(request):   
    return render(request, 'vitri11.html')
def vitri12(request):   
    return render(request, 'vitri12.html')
def vitri13(request):   
    return render(request, 'vitri13.html')
def vitri14(request):   
    return render(request, 'vitri14.html')
def vitri15(request):   
    return render(request, 'vitri15.html')
def vitri16(request):   
    return render(request, 'vitri16.html')
def vitri17(request):   
    return render(request, 'vitri17.html')
def vitri18(request):   
    return render(request, 'vitri18.html')
def vitri19(request):   
    return render(request, 'vitri19.html')
def vitri20(request):   
    return render(request, 'vitri20.html')
def vitri21(request):   
    return render(request, 'vitri21.html')
def vitri22(request):   
    return render(request, 'vitri22.html')
def vitri23(request):   
    return render(request, 'vitri23.html')
def vitri24(request):   
    return render(request, 'vitri24.html')
def vitri25(request):   
    return render(request, 'vitri25.html')
def vitri26(request):   
    return render(request, 'vitri26.html')
def vitri27(request):   
    return render(request, 'vitri27.html')
def vitri28(request):   
    return render(request, 'vitri28.html')
def vitri29(request):   
    return render(request, 'vitri29.html')
def vitri30(request):   
    return render(request, 'vitri30.html')
def vitri31(request):   
    return render(request, 'vitri31.html')
def vitri32(request):   
    return render(request, 'vitri32.html')
def vitri33(request):   
    return render(request, 'vitri33.html')
def vitri34(request):   
    return render(request, 'vitri34.html')
def vitri35(request):   
    return render(request, 'vitri35.html')
def vitri36(request):   
    return render(request, 'vitri36.html')  

   