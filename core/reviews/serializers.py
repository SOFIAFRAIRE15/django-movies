from rest_framework import serializers

from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
     """
        Serializer para POST 

        Ejemplo de JSON a enviar en POST:

        {
  
            "user": 1,
            "movie": 10, 
            "content":"Muy buena y entretenida pelicula de accion y drama donde se reflejan momentos de cotidianeidad"
  
        }
        
     """

     class Meta:
        model = Review
        fields = '__all__'




class ReviewDetailSerializer(serializers.ModelSerializer): 
    """
        Serializer para GET(Listar detalles)

         Ejemplo de respuesta JSON:

        {
    "id": 3,
    "user": "Sofia",
    "content": "Entretenida pelicula de accion y drama donde se reflejan momentos de cotidianeidad",
    "created_at": "2023-05-11T13:16:44.197193-03:00",
    "last_update": "2023-05-11T13:16:44.197193-03:00",
    "movie": {
      "id": 10,
      "name": "Relatos Salvajes",
      "year": 2014,
      "synopsis": "Un viaje en avión, el encuentro con alguien del pasado, un pinchazo en una carretera, una multa, un atropello o una boda; historias independientes con un denominador común: la violencia sin control ni causa aparente, que impulsa a perder el control. En seis episodios diferentes los personajes se verán empujados a situaciones al borde del abismo, perdiendo el control de sus vidas."
    }

    
    """
   
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields =  '__all__'
        depth = 1

