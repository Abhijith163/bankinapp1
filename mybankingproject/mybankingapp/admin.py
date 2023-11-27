from django.contrib import admin
from .models import District, Branch, UserProfile

# Register your models here.
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(UserProfile)

