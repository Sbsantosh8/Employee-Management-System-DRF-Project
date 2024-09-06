from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginAPIView, EmployeeCreateAPIView,EmployeeUpdateAPIView,EmployeeDetailAPIView
from .views import employee_delete



urlpatterns = [
    path('auth/login/', obtain_auth_token, name='api_token_auth'),
    path('employee/create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('employee/',EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/',EmployeeDetailAPIView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/update/',EmployeeUpdateAPIView.as_view(),name='employee-update'),
    path('employee/<int:pk>/delete/',employee_delete,name="employee-delete"),
    path('login/', LoginAPIView.as_view(), name='login'),

]
