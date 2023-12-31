from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item

EMPTY_LIST_ERROR = '빈 아이템을 등록할 수 없습니다.'
DUPLICATE_ITEM_ERROR = '이미 리스트에 해당 아이템이 있습니다.'


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
        if kwargs.get('for_list'):
            self.instance.list = kwargs['for_list']
        return super().save()


class ExistingListItemForm(ItemForm):

    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)
