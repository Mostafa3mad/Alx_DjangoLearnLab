from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


class LoginView(BaseLoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True  # Redirect if the user is already authenticated

# Logout View
class LogoutView(BaseLogoutView):
    template_name = 'relationship_app/logout.html'

##############################################################################


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Admin"
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html", {"role": "Admin"})




def is_librarian(user):
    if not user.is_authenticated:
        return False
    try:
        return user.userprofile.role == "Librarian"
    except UserProfile.DoesNotExist:
        return False@login_required


@user_passes_test(is_librarian)
def librarian_view(request):  # ✅ Ensure this function is named "librarian_view"
    return render(request, "relationship_app/librarian_view.html", {"role": "Librarian"})






def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == "Member"

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"role": "Member"})



@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html", {"role": "Member"})
