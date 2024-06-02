from django.shortcuts import render

# Create your views here.
def home(request):
    # obj = place.objects.all()

    return render(request, "index.html")