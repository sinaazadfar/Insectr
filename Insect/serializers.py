from rest_framework import serializers
from .models import Arthropod, Category, LayerOne, LayerTwo, LayerThree, Child

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'name', 'description', 'image')

class LayerThreeSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True)
    class Meta:
        model = LayerThree
        fields = ('id', 'name', 'children')

class LayerTwoSerializer(serializers.ModelSerializer):
    children = LayerThreeSerializer(many=True)
    class Meta:
        model = LayerTwo
        fields = ('id', 'name', 'children')

class LayerOneSerializer(serializers.ModelSerializer):
    children = LayerTwoSerializer(many=True)
    class Meta:
        model = LayerOne
        fields = ('id', 'name', 'children')

class CategorySerializer(serializers.ModelSerializer):
    children = LayerOneSerializer(many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'children')

class ArthropodSerializer(serializers.ModelSerializer):
    children = CategorySerializer(many=True)
    class Meta:
        model = Arthropod
        fields = ('id', 'name', 'children')
