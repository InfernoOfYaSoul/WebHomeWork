from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Info
from .forms import NameForm
from django.core.files.storage import default_storage



def first_page(request):
    return render(request, 'myapp/firstpage.html',)

def name_input(request):
    if request.method == "POST":
        form = NameForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if 'photo' in request.FILES:
                uploaded_file = request.FILES['photo']
                # print(type(uploaded_file))
                name = default_storage.save(uploaded_file.name, uploaded_file)
                url = default_storage.url(name)
                print(url)
                # print(data['photo'])
                # print(url)
                data['photo'] = url[7:]
                # print(data['photo']) [7:]
            data['birth_date'] = data['birth_date'].isoformat()
            request.session['first_page_data'] = data
            print("Save")
            return redirect('next_page')
        print("Post no save")
    else:
        form = NameForm()
        print("No post no save")
    return render(request, "myapp/firstpage.html", {"form": form})


def next_page(request):
    first_page_data = request.session.get('first_page_data', {})
    first_page_data = dict(list(first_page_data.items())[:7])
    first_page_data['photo'] = "../media/" + first_page_data['photo']

    sex = 'Девушка'
    name = first_page_data['name']
    if first_page_data['sex'] == "M":
        sex = "Парень"

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            second_page_data = form.cleaned_data
            second_page_data = dict(list(second_page_data.items())[7:])
            all_data = {**first_page_data, **second_page_data}
            print(all_data)
            print("Save2")
            form = Info(**all_data)
            form.save()
            form = NameForm(request.POST)
            return redirect('name_input')
        print("Post no save2")

    else:
        form = NameForm()
        print("No post no save2")
    return render(request, "myapp/secondpage.html", {"form": form, "url": first_page_data['photo'], "name": name, "sex": sex})
