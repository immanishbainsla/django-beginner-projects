from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text':'Hello World!!', 'number':100}
    return render(request, 'basicapp/index.html', context)


def other(request):
    return render(request, 'basicapp/other.html')


def relative(request):
    return render(request, 'basicapp/relativeurltemplates.html')
