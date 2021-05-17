from django.contrib import admin
from calculator.models import Bmi, Suggestion

# Register your models here.


@admin.register(Bmi)
class BmiAdmin(admin.ModelAdmin):
    list_display = ("weight","height","bmi",)

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("suggestion","message",)