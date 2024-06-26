from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,status
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class MovieViewSet (viewsets.ModelViewSet):
      queryset= Movie.objects.all()
      serializer_class = MovieSerializer

      @action(detail=True, methods=['POST'])
      def rate_movie(self, request, pk:None):
            if 'stars' in request.data:
                  movie = Movie.objects.get(id=pk)
                  print("movie title : ", movie.title)
                  response = {"message": 'its Working'}
                  return Response(response, status= status.HTTP_200_OK)
            else:
                  response = {"message": 'You need to provide stars'}
                  return Response(response, status= status.HTTP_400_BAD_REQUEST)
class RatingViewSet (viewsets.ModelViewSet):
      queryset= Rating.objects.all()
      serializer_class = RatingSerializer

# Create your views here.
