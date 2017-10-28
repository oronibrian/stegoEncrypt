from django.shortcuts import render

# Create your views here.
def index(request):
    title="Image steganoraphy"
    context={
        'title':title,
    }
    return render(request,'index.html',context)
