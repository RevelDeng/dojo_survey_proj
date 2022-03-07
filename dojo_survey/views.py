from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    context = {
        "name": request.POST.get("name", "N/A"),
        "location": request.POST.get("location", "N/A"),
        "language": request.POST.get("language", "N/A"),
        "likes": "N/A",
        "comment": request.POST.get("comment", "N/A")
    }

    if request.POST.get('likes1') and request.POST.get('likes2'):
        context["likes"] = request.POST['likes1'] + ", " + request.POST['likes2']
    elif request.POST.get('likes1') and request.POST.get('likes2') == None:
        context["likes"] = request.POST['likes1']
    elif request.POST.get('likes1') == None and request.POST.get('likes2'):
        context["likes"] = request.POST['likes2']

    return render(request, 'info.html', context)