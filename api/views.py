from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from fruit.models import Fruit
from .serializer import FruitSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


# Create your views here.

#region function base view

# CRUD
@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Fruit.objects.order_by('Capacity').all()
        todo_serializer = FruitSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail_view(request: Request, todo_id:int):
    try:
        todo = Fruit.objects.get(pk=todo_id)
    except Fruit.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FruitSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = FruitSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

# endregion

#region class base view

class FruitsListApiView(APIView):
    def get(self, request: Request):
        todos = Fruit.objects.order_by('Capacity').all()
        todo_serializer = FruitSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)


class FruitsDetailApiView(APIView):
    def get_object(self, todo_id: int):
        try:
            todo = Fruit.objects.get(pk=todo_id)
            return todo
        except Fruit.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)


    def get(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        serializer = FruitSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        serializer = FruitSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, todo_id:int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

#endregion

#region mixins

class FruitsListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Fruit.objects.order_by('Capacity').all()
    serializer_class = FruitSerializer

    def get(self, request: Request):
        return self.list(request)
    
    def post(self, request: Request):
        return self.create(request)


class FruitsDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Fruit.objects.order_by('Capacity').all()
    serializer_class = FruitSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

#endregion

#region generics

class FruitsGenericApiViewPagination(PageNumberPagination):
    page_size = 3

class FruitsGenericApiView(generics.ListCreateAPIView):
    queryset = Fruit.objects.order_by('Capacity').all()
    serializer_class = FruitSerializer
    pagination_class = FruitsGenericApiViewPagination
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class FruitsGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.order_by('Capacity').all()
    serializer_class = FruitSerializer

#endregion

#region viewsets

class FruitsViewSetApiView(viewsets.ModelViewSet):
    queryset = Fruit.objects.order_by('Capacity').all()
    serializer_class = FruitSerializer
    pagination_class = LimitOffsetPagination

#endregion

