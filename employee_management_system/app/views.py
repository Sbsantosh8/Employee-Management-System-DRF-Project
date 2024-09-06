from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import EmployeeCreationForm
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny




# # users = Employee.objects.all()

# # for user in users:
# #    token = Token.objects.get_or_create(user=user)
# #    print(token)

class EmployeeCreateAPIView(APIView):
  
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        # Render the form as HTML
        form = EmployeeCreationForm()
        return render(request, 'employee_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Handle form submission
        form = EmployeeCreationForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'status': 'Employee created'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)






class EmployeeDetailAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is not None:
            # Detail view
            try:
               
                employee = Employee.objects.get(pk=pk)
            except Employee.DoesNotExist:
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        else:
            # List view
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)




class EmployeeUpdateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        employee = Employee.objects.get(pk=pk)
        if not employee:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    emp_name = employee.first_name
    employee.delete()
    return Response({"message": f"Deleted Successfully  {emp_name}!"}, status=status.HTTP_204_NO_CONTENT)



class LoginAPIView(APIView):

    permission_classes = [AllowAny]  # Anyone can access this view
    
    def get(self,request):
        return render(request,"login.html")
    def post(self, request):
        # Get the username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)


        if user is not None:
            # Log the user in to create a session
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response({'message': 'Login successful', 'token': str(token)}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
