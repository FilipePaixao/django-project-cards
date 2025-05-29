from .models import Item, ItemForm
from django.shortcuts import render, redirect

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_item')
    else:
        form = ItemForm()
    return render(request, 'create.html', {'form': form})


def list_item(request):
    item = Item.objects.all()
    return render(request, 'list.html', {'item': item})