from django.urls import path
from . import views


urlpatterns = [
    path('user_groups/', views.UserProfile ,name='user_group'),
    path('group/', views.DongishGroupListAPIView.as_view(), name='group'),
    path('group/<int:pk>/', views.DongishGroupDetailAPIView.as_view()),
    path('group/<int:pk>/dutch', views.DongishGroupDutchCalculationAPIView, name='group_dutch'),
    path('transaction/', views.TransactionListAPIView.as_view(), name='transaction'),
    path('transaction/<int:pk>/', views.TransactionDetailAPIView.as_view()),
]