from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role, RoleUsers, Team, TeamUsers

admin.site.register(Role)
admin.site.register(RoleUsers)
admin.site.register(Team)
admin.site.register(TeamUsers)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'password']


admin.site.register(CustomUser, CustomUserAdmin)
