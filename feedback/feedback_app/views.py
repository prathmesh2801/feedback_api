from .serializers import FeedbackFormSerializer
from .models import FeedbackForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class FeedbackFormViews(APIView):

    def get(self, request, pk=None):
        if pk:
            feedback=FeedbackForm.objects.get(pk=pk)
            serializer=FeedbackFormSerializer(feedback)
            return Response (serializer.data,status=status.HTTP_200_OK)
        else :
            feedback=FeedbackForm.objects.all()
            serializer=FeedbackFormSerializer(feedback,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    def post(self, request):
        serializer = FeedbackFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Thank you for your Feedback!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        try:
            feedback=FeedbackForm.objects.get(pk=pk)
        except FeedbackForm.DoesNotExist:
            return Response("Feedback Form not found")
        
        serializer=FeedbackFormSerializer(feedback,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk):
        try:
            feedback=FeedbackForm.objects.get(pk=pk)
        except FeedbackForm.DoesNotExist:
            return Response("Feedback Form not found")
        
        serializer=FeedbackFormSerializer(feedback,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        feedback=FeedbackForm.objects.get(pk=pk)
        feedback.delete()
        return Response("Feedback Form deleted Successfully...!!",status=status.HTTP_204_NO_CONTENT)
