from django.contrib.auth.forms import UserCreationForm

# Django offers a lot of forms that you can use in your projects.
# One of them is UserCreationForm. It contains all the necessary fields to create a new user.
# However, it doesn't include an email field.

# But users need to configure an email address or else they won’t be able to receive password reset emails.
# To fix tht, we need to an 'email field' to the 'UserCreationForm' as follows--->

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)