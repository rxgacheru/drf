from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usadata.models import State, Person
from usadata.serializers import StateSerializer, PersonSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class StateList(APIView):
  def get(self, request, *args, **kwargs):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response({'status': 'success', 'states': serializer.data}, status=status.HTTP_200_OK)
   
  def post(self, request, *args, **kwargs):
    serializer = StateSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()

      return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response({'status': 'error', 'states': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  
class StateDetail(APIView):
    def get_object(self, id):
        try:
            return State.objects.get(id=id)
        except State.DoesNotExist:
            return None
        
    def get(self, request, id, *args, **kwargs):
        state = self.get_object(id)
        if state is None:
            return Response({'status': 'error', 'data': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StateSerializer(state)
        
        return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, id, *args, **kwargs):
        state = self.get_object(id)

        if state is None:
            return Response({'status': 'error', 'data': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
        state.delete()
        return Response({'status': 'success', 'data': 'State deleted successfully'}, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        state = self.get_object(id)
        serializer = StateSerializer(state, data=request.data)

        if serializer:
            return Response({'status': 'error', 'data': 'State not found'}, status=status.HTTP_404_NOT_FOUND)
        state.save()
        return Response({'status': 'success', 'data': 'State deleted successfully'}, status=status.HTTP_200_OK)
    

class PersonList(APIView):
    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response({
            'message': 'People retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Person created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error creating person',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class PersonList(APIView, PageNumberPagination):
    def get(self, request):
        people = Person.objects.all()
        results = self.paginate_queryset(people, request, view=self)
        serializer = PersonSerializer(results, many=True)
        return self.get_paginated_response({
            'message': 'People retrieved successfully',
            'people': serializer.data
        })

    def get(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response({
            'message': 'Person retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Person updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Error updating person',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = self.get_object(pk)
        person.delete()
        return Response({
            'message': 'Person deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)