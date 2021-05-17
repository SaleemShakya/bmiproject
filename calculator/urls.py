from django.urls import path
from calculator.views import suggest,bmi_add,bmi_list,bmi_edit,bmi_delete

app_name="bmi"

urlpatterns = [

    path("bmi-add/", bmi_add, name="bmi_add"),
    path("bmi-list/", bmi_list,name="bmi_list"),
    path("bmi-edit/<int:id>/", bmi_edit,name="bmi_edit"),
    path("bmi-delete/<int:id>/", bmi_delete,name="bmi_delete"),
    path("suggestions/",suggest, name="suggest")
]