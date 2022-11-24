from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from player_app.models import Player

from player_app.serializers import PlayerSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def player_list_or_add(request):
    if request.method=='GET':
        players = Player.objects.all()
        if(len(players)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PlayerSerializer(players, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = PlayerSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def player_details_or_update_or_delete(request, pk):
    try:
        player = Player.objects.get(id=pk)
    except Player.DoesNotExist:
        return JsonResponse({'message': 'The player does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    player=get_object_or_404(Player, id=pk)
    if request.method=='GET':
        serializer = PlayerSerializer(player, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = PlayerSerializer(player, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        player.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
@api_view(['GET'])
def player_age_gte(request, age_seuil):
    try:
        player = Player.objects.filter(age__gte=age_seuil)
        serializer = PlayerSerializer(player, context={'request': request}, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Player.DoesNotExist:
        return JsonResponse({'message': 'The player does not exist'}, status=status.HTTP_404_NOT_FOUND)