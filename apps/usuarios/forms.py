from django import forms
from django.core.exceptions import ValidationError

class LogonForms(forms.Form):
    nome_logon = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: John Doe"
            }
        )
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

def validate_x(sn):
        if sn:
            if "1" in sn:
                print(f'passou aqui 4.1')                   
                raise ValidationError("1 não são aceitos no campo senha.")
            else:
                print(f'passou aqui 4.2')                   
                return sn
        print(f'passou aqui 4.3') 

class CadastrarForms(forms.Form):
    nome=forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: John Doe"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: johndoe@mail.com"
            }
        )
    )
    senha_nova = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_novamente = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise ValidationError("Espaços não são aceitos no campo usuário.")
            else:
                return nome


    def clean_email(self):
        em = self.cleaned_data.get('email')
        if em:
            if "k" in em:
                raise forms.ValidationError("k não são aceitos no campo e-mail.")
            else:
                return em

    # É necessário fazer a validação no campo confirmacao 'novamente' porque senão a confirmacao não terá sido populada ainda ao se verificar na primeira senha.
    def clean_senha_novamente(self):
        senha1 = self.cleaned_data['senha_nova']
        senha2 = self.cleaned_data.get('senha_novamente')
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("Senhas não são iguais!")
            else:
                return senha2
            
    # def clean(self):
    #     # cleaned_data = super().clean()
    #     # nome = cleaned_data.get("nome_cadastro")
    #     print('passou aqui 5 ')        
    #     super().clean()
    #     nome =self.cleaned_data.get("nome_cadastro")      
    #     print(f'passou aqui 5.1 {nome}')          
    #     em = self.cleaned_data.get("senha_nova")
    #     print(f'passou aqui 5.2 {em}')
    #     if " " in nome:
    #         print('passou aqui 5.3 ') 
    #         self.add_error(None, "Espaços não são aceitos no campo usuário.")                   
    #         # raise ValidationError("Espaços não são aceitos no campo usuário.")
    #     if "1" in em:
    #         print('passou aqui 5.4 ')        
    #         self.add_error(None, "k não são aceitos no campo e-mail.")             
    #         # raise ValidationError("k não são aceitos no campo e-mail.")
    #         raise forms.ValidationError({"senha_nova": "raise an error"})
    #     return self.cleaned_data