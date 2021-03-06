from django import forms
from django.db import models
from django.urls import reverse
from users.models import CustomUser, Profile


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product_list_by_category', args=[self.slug])

RENT_DURATION = (
    ('One Day', 'One Day'),
    ('One Week', 'One Week'),
    ('One Month', 'One Month'),
)
class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    rent_duration = models.CharField(max_length=100, choices=RENT_DURATION)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product_detail', args=[self.id, self.slug])


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'description', 'price', 'rent_duration', 'image']

        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name', 'class':'form-control'}), required=True)
        slug = forms.SlugField(widget=forms.TextInput(attrs={'placeholder':'Product Slug', 'class':'form-control'}), required=True)
        category = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), required=True)
        description = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), required=True)
        price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}), required=True)
        image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}), required=True)
        rent_duration = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=RENT_DURATION, required=True)

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'description', 'price', 'rent_duration', 'image' ]

        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name', 'class':'form-control'}), required=True)
        slug = forms.SlugField(widget=forms.TextInput(attrs={'placeholder':'Product Slug', 'class':'form-control'}), required=True)
        category = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), required=True)
        description = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), required=True)
        price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}), required=True)
        image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}), required=True)
        rent_duration = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=RENT_DURATION, required=True)
