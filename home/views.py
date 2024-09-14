# home/views.py
from django.shortcuts import render
from home.tasks import add

def index(request):
    # Call the task asynchronously
    result = add.delay(10, 77)
    
    # Optionally, check if the task result is ready
    if result.ready():
        print(f'Task result: {result.get()}')  # Get result when task is finished
    else:
        print('Task is still running...')
    
    return render(request, 'index.html', {})
