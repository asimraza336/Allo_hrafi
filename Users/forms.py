from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from Users.models import User
from AdminApp.models import City, ServiceImage, Service

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        # provider_user = kwargs.pop('provider_user', None)
        # user = [0]
        super(ServiceForm, self).__init__(*args, **kwargs)
        # self.fields['provider_user'].queryset = User.objects.filter(id=provider_user)
        # self.fields['provider_user'].value = User.objects.get(id=provider_user)
        self.fields['provider_user'].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control sf-form-control'
        # self.fields['category_id'].widget.attrs['class'] = 'form-control sf-form-control'
        # self.fields['category_id'].widget.attrs['placeholder'] = 'Category Name'
        

class ServiceImageForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ServiceImage
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        
        super(ServiceImageForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control sf-form-control'



class SignUpForm(UserCreationForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='Select the City')
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('user_role', 'username', 'first_name', 'last_name', 'email', 'phone_number',
                  'gender', 'city', 'address', 'profile_picture',  'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control sf-form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        
        self.fields['last_name'].widget.attrs['class'] = 'form-control sf-form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        
        self.fields['user_role'].widget.attrs['class'] = 'form-control sf-form-control'
        self.fields['user_role'].widget.attrs['placeholder'] = 'User Role'
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number (05352-xxxxx)'
        
        self.fields['gender'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['placeholder'] = 'Gender'
        
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['placeholder'] = 'Address'
        
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
        self.fields['profile_picture'].widget.attrs['placeholder'] = 'Profile Picture'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=300, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter UserName'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'