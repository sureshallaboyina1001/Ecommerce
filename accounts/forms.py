from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name','email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name','email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]





class GuestForm(forms.Form):
     email    = forms.EmailField()

class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


    # def form_valid(self, form):
    #     request = self.request
    #     next_ = request.GET.get('next')
    #     next_post = request.POST.get('next')
    #     redirect_path = next_ or next_post or None
    #     email  = form.cleaned_data.get("email")
    #     password  = form.cleaned_data.get("password")
        
    #     print(user)
    #     if user is not None:
    #         if not user.is_active:
    #             print('inactive user..')
    #             messages.success(request, "This user is inactive")
    #             return super(LoginView, self).form_invalid(form)
    #         login(request, user)
    #         user_logged_in.send(user.__class__, instance=user, request=request)
    #         try:
    #             del request.session['guest_email_id']
    #         except:
    #             pass
    #         if is_safe_url(redirect_path, request.get_host()):
    #             return redirect(redirect_path)
    #         else:
    #             return redirect("/")
    #     return super(LoginView, self).form_invalid(form)
class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name','email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #user.active = False
        if commit:
            user.save()
        return user




   



