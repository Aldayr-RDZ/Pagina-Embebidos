from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from alarmas.models import Alarma
from alarmas.api.serializers import AlarmaSerializer

@api_view(['GET','POST'])
def alarma_api_view(request):
    if request.method == 'GET':
        alarmas = Alarma.objects.all()
        alarmas_serializer = AlarmaSerializer(alarmas, many= True)
        return Response(alarmas_serializer.data)
    
    elif request.method == 'POST':
        alarma_serializer=AlarmaSerializer(data= request.data)
        if alarma_serializer.is_valid():
            alarma_serializer.save()
            return Response(alarma_serializer.data)
        return Response(alarma_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def alarma_detail_view(request,pk=None):
    if request.method == 'GET':
        alarma= Alarma.objects.filter(idAlarma=pk).first()
        alarma_serializer = AlarmaSerializer(alarma)
        return Response(alarma_serializer.data)
    
    elif request.method == 'PUT':
        alarma= Alarma.objects.filter(idAlarma=pk).first()
        alarma_serializer = AlarmaSerializer(alarma, data=request.data)
        if alarma_serializer.is_valid():
            alarma_serializer.save()
            return Response(alarma_serializer.data)
        return Response(alarma_serializer.errors)

    elif request.method == 'DELETE':
        alarma= Alarma.objects.filter(idAlarma=pk).first()
        alarma.delete()
        return Response('Eliminado')