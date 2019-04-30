from rest_framework import viewsets, filters, permissions
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUsers.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.kwargs['user_name']
        print(name)
        passwd = self.kwargs['pass']
        print(passwd)
        return AppUsers.objects.filter(user_name=name,user_password=passwd)
        

class EncodeViewSet(viewsets.ModelViewSet):
    queryset = EncodedData.objects.all()
    serializer_class = EncodeSerializer
    

class ScanViewSet(viewsets.ModelViewSet):
    queryset = ScanData.objects.all()
    serializer_class = ScanSerializer


@api_view(['POST'])
def studentLogin(request,format=None):
    if request.method == "POST":
        try:
            encData = EncodedData.objects.get(user_name=request.data['user_name'])
            serializer = EncodeSerializer(encData)

            pos = ScanData.objects.filter(encoded_text = serializer.data['encoded_text'])
            serializer1 = ScanSerializer(pos, many=True)

            return Response(serializer1.data,status=status.HTTP_200_OK)
        except EncodedData.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)