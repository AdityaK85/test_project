from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from six import text_type

class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
    def validate(self, obj): 
        self.user = obj 
        refresh = self.get_token(self.user) 
        data = {}
        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token) 
        return data

