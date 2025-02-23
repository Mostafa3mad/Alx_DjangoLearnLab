from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_librarian(user):
    if not user.is_authenticated:
        return False
    try:
        return user.userprofile.role == "Librarian"
    except UserProfile.DoesNotExist:
        return False

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html", {"role": "Librarian"})
