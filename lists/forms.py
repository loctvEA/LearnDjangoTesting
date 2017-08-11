from django import forms
from lists.models import Item

EMPTY_LIST_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm):

    text = forms.CharField(required=False, widget=forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg'
            }))

    class Meta:
        model = Item
        fields = ('text', )
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError(EMPTY_LIST_ERROR)
        return

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()
