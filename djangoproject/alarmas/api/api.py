import rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from alarmas.models import Alarma
from alarmas.api.serializers import AlarmaSerializer

@api_view(['GET','POST'])
def alarma_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        alarmas = Alarma.objects.all()
        alarmas_serializer = AlarmaSerializer(alarmas, many= True)
        return Response(alarmas_serializer.data, status = status.HTTP_200_OK)
    #create
    elif request.method == 'POST':
        alarma_serializer=AlarmaSerializer(data= request.data)
        #validacion
        if alarma_serializer.is_valid():
            alarma_serializer.save()
            return Response({'message': 'Alarma registrada correctamente!'}, status= status.HTTP_201_CREATED)
        
        return Response(alarma_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def alarma_detail_view(request,pk=None):
    alarma= Alarma.objects.filter(idAlarma=pk).first()
    if alarma:
            #retrieve
        if request.method == 'GET':
            alarma_serializer = AlarmaSerializer(alarma)
            return Response(alarma_serializer.data, status = status.HTTP_200_OK)
            #update
        elif request.method == 'PUT':
             alarma_serializer = AlarmaSerializer(alarma, data=request.data)
             if alarma_serializer.is_valid():
                 alarma_serializer.save()
                 return Response(alarma_serializer.data,status = status.HTTP_200_OK)
             return Response(alarma_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #delete
        elif request.method == 'DELETE':
            alarma= Alarma.objects.filter(idAlarma=pk).first()
            alarma.delete()
            return Response({'message': 'Alarma eliminada correctamente!'},status = status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una alarma con estos datos'},status= status.HTTP_400_BAD_REQUEST)