from django.shortcuts import render
from app1.models import Movie
from app1.forms import appform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.

# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})

class MovieList(ListView):
    model=Movie
    template_name = "home.html"
    context_object_name = "m"


# def addmore(request):
#     if (request.method == "POST"):  # after submission
#         form =appform(request.POST,request.FILES)  # creates form object initialized with values inside request.POST
#         if form.is_valid():
#             form.save()  # saves form objects in db model Book
#             return home(request)
#     form = appform()
#     return render(request, 'addmore.html', {'form': form})

class Movieadd(CreateView):
    model = Movie
    template_name = "addmore.html"
    fields = "__all__"
    success_url = reverse_lazy("app1:home")


# def details(request,p):
#     m =Movie.objects.get(id=p)
#     return render(request, 'details.html', {'m': m})

class MovieDetail(DetailView):
    model = Movie
    template_name = "details.html"
    context_object_name = "m"



# def update(request,p):
#     m=Movie.objects.get(id=p)
#     if (request.method == "POST"):
#         form=appform(request.POST,request.FILES,instance=m)
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#     form=appform(instance=m)
#     return render(request,'update.html',{'form': form})

class Movieupdate(UpdateView):
    model = Movie
    template_name = "update.html"
    fields = "__all__"
    success_url = reverse_lazy("app1:home")


# def delete(request,p):
#     m=Movie.objects.get(id=p)
#     m.delete()
#     return home(request)

class Moviedelete(DeleteView):
    model=Movie
    success_url=reverse_lazy("app1:home")
    template_name="delete.html"

