from django import forms

from home.models import Order
from product.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'name', 'phone', 'comment',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name','surname','phone','amount','category', 'food', 'address',)