from django.contrib.auth.models import User
from django.http import Http404

from quickstart.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_auth.views import LoginView
from rest_framework.exceptions import ParseError, ValidationError, AuthenticationFailed
from rest_framework import serializers

class UserList(APIView):
	def get(self, request, format=None):
	    users = User.objects.all()
	    serializer = UserSerializer(users, many=True)
	    return Response(serializer.data)

	def post(self, request, format=None):
	    serializer = UserSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data, status=status.HTTP_201_CREATED)
	    else:
    		raise ValidationError()
	    	#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
	    user = self.get_object(pk)
	    user.delete()
	    return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
	def get_object(self, pk):
	    try:
	        return User.objects.get(pk=pk)
	    except User.DoesNotExist:
	        raise Http404

	def get(self, request, pk, format=None):
	    user = self.get_object(pk)
	    user = UserSerializer(user)
	    return Response(user.data)

	def put(self, request, pk, format=None):
	    user = self.get_object(pk)
	    serializer = UserSerializer(user, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
	    user = self.get_object(pk)
	    user.delete()
	    return Response(status=status.HTTP_204_NO_CONTENT)
