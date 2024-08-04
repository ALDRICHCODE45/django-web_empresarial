from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "escribe tu nombre"}
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Escribe tu email"}
        ),
    )
    content = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Escribe el contenido",
            }
        ),
    )
