from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from crud_task.models import tasktable
from .serializers import tasktableSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import TaskForm
from rest_framework import status
from rest_framework.views import APIView
    
def homepage(req):
    return render(req,'homepage.html')


 
'''     
@api_view(['POST', 'GET','DELETE'])
def createtask(request):
    if request.method == 'GET':
        task = tasktable.objects.all()
        serializer = tasktableSerializer(task, many=True)
        # form = TaskForm()  # Create an instance of the form
        # return render(request, 'datashow.html', {'tasks': serializer.data, 'form': form})
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serial=tasktableSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        
    elif request.method=='DELETE':
        alldata=tasktable.objects.all().delete()
        return  Response({"all data deleted ssuccesfully "},status=status.HTTP_400_BAD_REQUEST) '''

class createtask(APIView):
    serializer_class = tasktableSerializer

    def get(self, request):
        tasks = tasktable.objects.all()
        serializer = tasktableSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = tasktableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        tasktable.objects.all().delete()
        return Response({"all data deleted successfully"}, status=status.HTTP_200_OK)
  
 
'''   
@api_view(['GET', 'PUT','DELETE'])
def update_task(request, pk):
    taskinstance = get_object_or_404(tasktable, pk=pk)

    if request.method == 'GET':
        serializer = tasktableSerializer(taskinstance)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = tasktableSerializer(taskinstance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        count=taskinstance.delete()
        return Response({"data deleted succefully {count[0]}"},status=status.HTTP_204_NO_CONTENT)
 

 '''
class update_task(APIView):
    serializer_class = tasktableSerializer
    
    def get(self, request, pk):
        task_instance = get_object_or_404(tasktable, pk=pk)
        serializer = tasktableSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task_instance = get_object_or_404(tasktable, pk=pk)
        serializer = tasktableSerializer(task_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task_instance = get_object_or_404(tasktable, pk=pk)
        count = task_instance.delete()
        return Response({"data deleted successfully": count[0]}, status=status.HTTP_204_NO_CONTENT) 

        
        