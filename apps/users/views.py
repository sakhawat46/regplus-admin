from django.views.generic import TemplateView, ListView
from web_project import TemplateLayout
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from .forms import UserCreateForm, UserUpdateForm

User = get_user_model()


class UserView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class UserListView(ListView):
    model = User
    template_name = 'user_list_basic.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initialize TemplateLayout if needed
        context = TemplateLayout.init(self, context)

        # Add additional pagination context
        if context.get('page_obj'):
            context['users'] = context['page_obj']
        return context


class UserCreateView(CreateView):
    template_name = 'edit_user.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user_create_success')

    def get_success_url(self):
        # After the user is created, we can access it via self.object
        return reverse_lazy('user_create_success', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

class UserCreateSuccessView(UserView):
    template_name = 'user_create_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        context['created_user'] = user
        return context



class UserUpdateView(UpdateView):
    template_name = 'edit_user.html'
    form_class = UserUpdateForm
    model = User

    def get_success_url(self):
        return reverse_lazy('user_create_success', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context



class UserDeleteView(UserView):
    template_name = 'user_confirm_delete.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        user = self.get_object()
        context['user'] = user
        context["object"] = user

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        try:
            username = user.username
            user.delete()
            messages.success(request, f'User "{username}" was deleted successfully.')
            return redirect(reverse('user-list'))
        except Exception as error:
            messages.error(request, f'Error deleting user: {error}')
            return redirect(reverse('user-list'))
