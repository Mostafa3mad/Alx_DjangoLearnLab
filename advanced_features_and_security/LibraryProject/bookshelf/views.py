from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Post

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
    return render(request, 'edit_post.html', {'post': post})
