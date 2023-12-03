from django.shortcuts import render, redirect
from .models import Mebel  # для чего здесь точка перед models?
from .forms import UpdateItemForm
from django.contrib.auth.forms import UserCreationForm  # последние три для регистрации пользователя
from django.views.generic.edit import CreateView  # последние три для регистрации пользователя
from django.urls import reverse_lazy  # последние три для регистрации пользователя
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404


def show_all(request):
    mebels = Mebel.objects.all().order_by('-price')
    paginator = Paginator(mebels, 20, orphans=5)

    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.get_page(page)
        current_page_list = current_page.object_list
    except InvalidPage as e:
        raise Http404(str(e))

    context = {
        'mebels': current_page_list,
        'is_paginated': is_paginated,
        'paginator': paginator
    }
    return render(request, 'app1/show_all.html', context)



def show_all_admin(request):
    form = UpdateItemForm()
    mebels = Mebel.objects.all().order_by('-price')
    paginator = Paginator(mebels, 20, orphans=5)

    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.get_page(page)
        current_page_list = current_page.object_list
    except InvalidPage as e:
        raise Http404(str(e))

    context = {
        'form': form,
        'mebels': current_page_list,
        'is_paginated': is_paginated,
        'paginator': paginator
    }
    return render(request, 'app1/show_admin_item.html', context)



def show_item(request, item_id):  # метод вывода позиции по id
    item = Mebel.objects.get(pk=item_id)  # pk -- это primary key
    return render(
        request,
        'app1/show_item.html',
        {'item': item}
    )



def update_item(request, item_id):
    if request.method == 'POST':
        new_description = dict(request.POST).get('description', '')
        new_price = dict(request.POST).get('price', '')
        Mebel.objects.filter(pk=item_id).update(
            price=new_price[0],
            description=new_description[0]
        )
    return redirect('items_admin')



def delete_item(request, item_id):
    Mebel.objects.filter(pk=item_id).delete()
    return redirect('items_admin')



def main(request):  # это добавили 02.11.2023
    return redirect('main')



def page_not_found(request, *args, **argv):  # это добавили 02.11.2023
    return redirect('main')



def login(request):
    return render(request,'app1/login.html')



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
