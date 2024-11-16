from django.shortcuts import render, redirect , get_object_or_404
from .models import Watches
from .forms import WatchForm
from django.contrib import messages
# Create your views here.

def all_watches(request):
    watches = Watches.objects.all() 
    context = {
        'watches': watches
    }
    return render(request, 'all_watches.html', context)



def create_watch(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_watches')
        else:
            return redirect('create_watch')
    else:
        form = {
            'watch_form': WatchForm()
        }
        return render(request, 'create_watch.html', form)



def detail_watch(request, pk):
    watch = get_object_or_404(Watches, id=pk)
    context = {
        'watch': watch
    }
    return render(request, 'detail_watch.html', context)



def update_watch(request, pk):
    watch = get_object_or_404(Watches, id=pk)
    if request.method == "POST":
        form = WatchForm(request.POST, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('detail_watch', watch.pk)
        else:
            for price in form.errors:
                messages.error(request, WatchForm.errors[price])
                return redirect(request.path)
    else:
        form = WatchForm(instance=watch)

        context = {
            'watch_form': form
        }
        return render(request, 'update_watch.html', context)

def delete_watch(request, pk):
    watch = get_object_or_404(Watches, id=pk)
    watch.delete()
    messages.success(request, 'Melumat ugurla silindi')
    return redirect('all_watches')






 




