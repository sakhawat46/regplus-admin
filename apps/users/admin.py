from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# class UserAdmin(UserAdmin):
#     # Fields to include in the add user form
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )

#     # Fields to include in the change user form
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'user_type')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#     )

#     # Fields to display in the user list
#     list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'user_type', 'created_at')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'user_type')
#     search_fields = ('email', 'username', 'first_name', 'last_name')
#     ordering = ('email',)

#     # Automatically exclude non-editable fields (like created_at) from the form
#     def get_readonly_fields(self, request, obj=None):
#         readonly_fields = super().get_readonly_fields(request, obj)
#         return readonly_fields + ('created_at',)

admin.site.register(User)
admin.site.register(Profile)
