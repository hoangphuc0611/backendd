from rest_framework import serializers
from .models import City,QH



class CitySerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.CharField(max_length=100)


    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    # def update(self,instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
    class Meta:
        model = City
        # fields = ['id','title','author','email']
        fields = '__all__'


class QHSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.CharField(max_length=100)


    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    # def update(self,instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
    class Meta:
        model = QH
        # fields = ['id','title','author','email']
        fields = '__all__'