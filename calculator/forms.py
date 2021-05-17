from django import forms
from calculator.models import Bmi

class BmiForm(forms.ModelForm):

    class Meta:

        model = Bmi
        fields = "__all__"
        exclude = ("bmi",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs["class"] = "form-control"