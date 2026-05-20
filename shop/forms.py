from django import forms
from .models import PaymentProof


class PaymentProofForm(forms.ModelForm):
    class Meta:
        model = PaymentProof
        fields = ['text_proof', 'file_proof']

    def clean_file_proof(self):
        file = self.cleaned_data.get("file_proof")

        if file:
            allowed_extensions = ('.png', '.jpg', '.jpeg', '.pdf')

            if not file.name.lower().endswith(allowed_extensions):
                raise forms.ValidationError("Only PNG, JPG, JPEG, and PDF files are allowed.")

        return file