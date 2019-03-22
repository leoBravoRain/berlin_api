from rest_framework import serializers
from .models import Food


# Serializer of Food
class Food_Serializer(serializers.ModelSerializer):

	class Meta:

		model = Food
		fields = '__all__'
