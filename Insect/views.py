from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChildSerializer, LayerThreeSerializer, LayerTwoSerializer, LayerOneSerializer, CategorySerializer, ArthropodSerializer
from .models import Child, LayerThree, LayerTwo, LayerOne, Category, Arthropod

@api_view(['GET', 'POST'])
def child_list(request):
    if request.method == 'GET':
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def child_detail(request, pk):
    try:
        child = Child.objects.get(pk=pk)
    except Child.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChildSerializer(child)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChildSerializer(child, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        child.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def layer_three_list(request):
    if request.method == 'GET':
        layer_threes = LayerThree.objects.all()
        serializer = LayerThreeSerializer(layer_threes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LayerThreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def layer_three_detail(request, pk):
    try:
        layer_three = LayerThree.objects.get(pk=pk)
    except LayerThree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LayerThreeSerializer(layer_three)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LayerThreeSerializer(layer_three, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        layer_three.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def layer_two_list(request):
    if request.method == 'GET':
        layer_twos = LayerTwo.objects.all()
        serializer = LayerTwoSerializer(layer_twos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LayerTwoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def layer_two_detail(request, pk):
    try:
        layer_two = LayerTwo.objects.get(pk=pk)
    except LayerTwo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LayerTwoSerializer(layer_two)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LayerTwoSerializer(layer_two, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        layer_two.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def layer_one_list(request):
    if request.method == 'GET':
        layer_ones = LayerOne.objects.all()
        serializer = LayerOneSerializer(layer_ones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LayerOneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def layer_one_detail(request, pk):
    try:
        layer_one = LayerOne.objects.get(pk=pk)
    except LayerOne.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LayerOneSerializer(layer_one)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LayerOneSerializer(layer_one, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        layer_one.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST'])
def arthropod_list(request):
    if request.method == 'GET':
        arthropods = Arthropod.objects.all()
        serializer = ArthropodSerializer(arthropods, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArthropodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def arthropod_detail(request, pk):
    try:
        arthropod = Arthropod.objects.get(pk=pk)
    except Arthropod.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArthropodSerializer(arthropod)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArthropodSerializer(arthropod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        arthropod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

