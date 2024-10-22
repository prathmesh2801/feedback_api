from .views import FeedbackFormViews
from django.urls import path


urlpatterns = [
    path('feedback/', FeedbackFormViews.as_view(),),
    path('feedback/<int:pk>/', FeedbackFormViews.as_view()),
]


