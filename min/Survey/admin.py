from django.contrib import admin
from .models import UserCostume,Question,option


admin.site.register(UserCostume)
admin.site.register(option)


admin.site.register(Question)