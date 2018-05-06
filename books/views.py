from django.shortcuts import render, redirect, get_object_or_404
from .forms import bookForm
from .models import book
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required#(login_url='/login/')
def booklist(request):
    book1 = book.objects.all()
    context = {'book':book1}
    return render(request, "home.html", context)

@login_required#(login_url='/login/')
def addbook(request):
    if request.method == 'POST':
        form = bookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = bookForm()
    return render(request, "addbook.html", {'form':form})

#@login_required#(login_url='/login/')
def bookdetail(request, id=None): #retrive
    instance = get_object_or_404(book, pk=id)
    context = { 'instance': instance,}
    return render(request, 'bookdetail.html', context)

@login_required#(login_url='/login/')    
def updatebook(request, id=None):
    instance = get_object_or_404(book, pk=id)
    form = bookForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('booklist')
    context = {'instance': instance, 'form': form,}
    return render(request, "addbook.html", {'context': context})
    