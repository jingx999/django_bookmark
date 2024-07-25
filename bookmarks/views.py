from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bookmark
from .forms import BookmarkForm


def home(request):
    hello = 'hello'
    return render(request, 'bookmarks/home.html', {'hello':hello})


# 只有登录用户才能看到书签列表
@login_required
def bookmark_list(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'bookmarks/bookmark_list.html', {'bookmarks': bookmarks})

@login_required
def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(data=request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            return redirect('bookmarks:bookmark_list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/bookmark_form.html', {'form': form})

@login_required
def bookmark_edit(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookmarkForm(instance=bookmark, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmarks:bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmarks/bookmark_form.html', {'form': form})

@login_required
def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmarks:bookmark_list')
    return render(request, 'bookmarks/bookmark_confirm_delete.html', {'bookmark': bookmark})
