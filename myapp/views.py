from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# 메인
def main(request):    
    return render(request, 'myapp/main.html')

# 소개   
def intro(request):
    return render(request, 'myapp/intro.html')

# 옷고르기   
def cloth(request):
    return render(request, 'myapp/undecided.html')
    
# 카메라
def webcam(request):
	return render(request, 'myapp/webcam.html')