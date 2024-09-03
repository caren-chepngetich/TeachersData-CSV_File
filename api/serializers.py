from rest_framework import serializers
from trainer.models import Trainer
from kicdofficial.models import Kicdofficial  
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

class KicdofficialSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Kicdofficial  # Ensure this matches your model name
        fields = "__all__"
