from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

#モデルを継承しないフォームクラス
class YearMonthForm(forms.Form):
    year    = forms.IntegerField()
    month   = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])

class YearForm(forms.Form):
    year    = forms.IntegerField()

class MonthForm(forms.Form):
    month   = forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(12)])
