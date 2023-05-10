from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
def index_movies(request):
    return JsonResponse({"message": "OnLine"})


class MovieView(APIView):
    def get (self, request, pk = None):
        if pk:
            #movie = Movie.objects.get(pk=pk)
            movie = get_object_or_404(Movie, pk=pk)
            serializers = MovieSerializer(movie)
        else:
           movies = Movie.objects.all()
           serializers = MovieSerializer(movies, many = True)
        return Response(serializers.data)


    def post (self, request):
        #JSON de la petición
        print(request.data)
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            




    def put (self, request, pk = None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else: 
             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  

    def delete (self, request, pk = None):
        if pk: 
            movie = get_object_or_404(Movie, pk=pk)
            movie.delete()
        else:
            return Response(
                {"msg": "Necesitas enviar el ID de la pelicula a eliminar"},
                status = status.HTTP_400_BAD_REQUEST
            )
        return Response({"msg": f"Pelicula con ID {pk} eliminada"})


