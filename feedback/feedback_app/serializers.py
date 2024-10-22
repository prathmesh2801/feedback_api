from rest_framework import serializers
from .models import FeedbackForm

class FeedbackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedbackForm
        fields="__all__"


    def validate_phone_number(self, value):
        if len(str(value)) != 10 :
            raise serializers.ValidationError("Please enter your valid 10 digit mobile number")
        return value