from django import forms

from lists.models import Item

EMPTY_LIST_ERROR = '빈 아이템을 등록할 수 없습니다.'


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': '작업 아이템 입력',
                'class': 'form-control',
            })
        }
        error_messages = {
            'text': {'required': EMPTY_LIST_ERROR}
        }

    def save(self, commit=False, **kwargs):
        self.instance.list = kwargs['for_list']
        return super().save()
