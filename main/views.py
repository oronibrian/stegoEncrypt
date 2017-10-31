from django.shortcuts import render
from .models import  HelpInstruction


# Create your views here.
def index(request):
    title="Image steganoraphy"
    context={
        'title':title,
    }
    return render(request,'index.html',context)


def helpfunc(request):
    instruction = HelpInstruction.objects.all()
    title = "User Instructions"

    context = {
        'title': title,
        'instructions': instruction,

    }
    return render(request, 'help.html', context)
