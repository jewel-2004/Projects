from django.shortcuts import render,redirect,get_object_or_404

from .models import student
from .forms import studentform,RegisterForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'index.html')


def reshome(request):
    return render(request, 'reshome.html')


def Home(request):
    return render(request, 'home.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

#read
def student_list(request):
    students = student.objects.all()
    return render(request, 'student_list.html', {'students': students})

#create
def  add_student(request):
    form=studentform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render (request, 'add_student.html',{'form':form})

#update
def edit_student(request,pk):
    std = get_object_or_404(student,pk=pk)
    form = studentform(request.POST or None,instance=std)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render (request, 'edit_student.html',{'form':form})


#delete

def  delete_student(request,pk):
    s = get_object_or_404(student,pk=pk)
    if request.method=='POST' :
        s.delete()
        return redirect('student_list')
    return render (request,'delete_student.html',{'student':s})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()  # for GET request

    return render(request, 'reg.html', {'form': form})

 
   

