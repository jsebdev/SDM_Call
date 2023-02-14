# from django.apps import apps
from django.contrib import admin

from .models import Call


@admin.register(Call)
class ProfileAdmin(admin.ModelAdmin):
    model = Call
    list_display = ('prompt', 'width', 'height', 'model', 'initial_image',
                    'number_of_samples', 'seed', 'num_outputs', 'called_at')


# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     model = Item
#     list_display = ('id', 'title', 'price', 'published',
#                     'seller', 'description')
#     list_filter = ('published', 'price', 'seller', 'tags')
#     list_editable = ('title', 'published', 'description', 'price')
#     search_fields = ('title', 'description', 'subtitle')
#     date_hierarchy = 'date_created'
#     save_on_top: bool = True


# app = apps.get_app_config("graphql_auth")
# for model_name, model in app.models.items():
#     admin.site.register(model)
