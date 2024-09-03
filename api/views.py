from rest_framework.response import Response
from rest_framework.views import APIView
from teacher.models import Teacher
from .serializers import TeacherSerializer
from trainer.models import Trainer
from .serializers import TrainerSerializer
from kicdofficial.models import Kicdofficial
from .serializers import KicdofficialSerializer 

# Create your views here.

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class TrainerListView(APIView):
    def get(self, request):
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return Response(serializer.data)

class KicdofficialListView(APIView):  
    def get(self, request):
        kicdofficials = Kicdofficial.objects.all()  
        serializer = KicdofficialSerializer(kicdofficials, many=True)
        return Response(serializer.data)
