from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "student_id",
        "name",
        "mobile",
        "branch",
    )

    search_fields = (
        "student_id",
        "name",
    )