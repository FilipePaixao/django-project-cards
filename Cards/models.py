from django.db import models
from django import forms
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField() 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(max_length=250, blank=True, null=True)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'price', 'description', 'images']
        
    def __str__(self):
        return self.name
        
    
    def total_price(self):
        return self.quantity * self.price