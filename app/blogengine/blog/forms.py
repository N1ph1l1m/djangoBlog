from django import forms
from .models import Tag,Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)

    # title.widget.attrs.update({'class':'form-control'})
    # slug.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Tag
        fields = ['title','slug']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()


        if new_slug == 'create':
            raise ValidationError('Slug mat not be "Create "')
        if Tag.objects.filter(slug__iexact= new_slug).count():
            raise ValidationError('Slug must be unique. We gace "{}" slug already'.format(new_slug))
        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(title = self.cleaned_data['title'], slug = self.cleaned_data['slug'])
    #     return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug' , 'bodu' , 'tags',]

        widget = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'bodu':forms.Textarea(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-control'}),



        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()


        if new_slug == 'create':
            raise ValidationError('Slug mat not be "Create "')
        return new_slug


        #  title = models.CharField(max_length = 150, db_index = True)
        # slug = models.SlugField(max_length = 150, unique = True)
        # bodu = models.TextField(blank = True, db_index = True)
        # date_pub = models.DateTimeField(auto_now_add = True)
        # tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
