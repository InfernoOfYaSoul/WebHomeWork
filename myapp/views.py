from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Info
from .forms import NameForm

def first_page(request):
    return render(request, 'myapp/firstpage.html',)

def next_page(request):
    return render(request, 'myapp/secondpage.html',)
    return redirect('next_page')

def name_input(request):
    if request.method == "POST":
        form = NameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('next_page')
    else:
        form = NameForm()
    return render(request, "myapp/firstpage.html", {"form": form})

# def post_list(request):
#     posts = Post.objects.order_by('published_date')
#     return render(request, 'myapp/ex.html', {'posts': posts})
    
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'myapp/post_detail.html', {'post': post})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'myapp/post_edit.html', {'form': form})

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'myapp/post_edit.html', {'form': form})
