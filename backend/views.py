from backend.models import Employee
from backend.serializers import EmployeeSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def registerEmployee(request):
    # import ipdb;ipdb.set_trace()
    data=request.data
    if data['name'] is not None:
        employee = Employee.objects.create(
            username=data['name'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            name=data['name'],
            email=data['email'],
            password=make_password(data['password']))
        serializer = EmployeeSerializer(employee, many=False)
        return Response(serializer.data)
    elif Employee.objects.filter(email=data['email']):
        message = {'detail': 'Employee with this Email Already exists'}
        return Response(message)
    elif Employee.objects.filter(name=data['name']):
        message = {'detail': 'Employee with this name Already exists'}
        return Response(message)
    else:
        message = {'detail': 'Server Error'}
        return Response(message)

@api_view(['GET'])
def getEmployees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEmployeeById(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

'''
{
    "name":"VSSatej",
    "first_name":"Satyan",
    "last_name":"Satyan",
    "email":"satej@gmail.com",
    "password":"CargoFL"
}
'''