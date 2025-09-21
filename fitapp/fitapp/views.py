from django.http import HttpResponse


def homepage(request):
    print(f'This is request + {request}') 
    return HttpResponse('Hello World. I am home.')
    

def about(request):
    return HttpResponse('My about page.')

  