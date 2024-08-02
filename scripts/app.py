import flet as ft
from flet import *

def create_base_container(content):
    return ft.Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=ft.Stack(
            width=300,
            height=550,
            controls=[content]
        )
    )

def main(page: ft.Page):
    page.title = "Expense Automate App"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def login_click(e):
        username = username_login.value
        password = password_login.value
        # Aqui você pode adicionar a lógica para verificar o login
        if username == "admin" and password == "admin":
            page.controls.clear()
            page.add(create_base_container(home_page(username)))
        else:
            page.add(ft.Text("Usuário ou senha incorretos. Tente novamente!", color='red'))
        page.update()

    def signup_click(e):
        username = username_signup.value
        password = password_signup.value
        if username == "" or password == "":
            page.add(ft.Text("Todos os campos devem ser preenchidos", color='red'))
        else:
            page.add(ft.Text(f"Usuário {username} registrado com sucesso!", color='green'))
        page.update()

    def switch_to_login(e):
        username_login.value = ""
        password_login.value = ""
        page.controls.clear()
        page.add(create_base_container(login_form))
        page.update()

    def switch_to_signup(e):
        username_signup.value = ""
        password_signup.value = ""
        page.controls.clear()
        page.add(create_base_container(signup_form))
        page.update()

    def home_page(username):
        return ft.Column(
            controls=[
                ft.Text(f"Olá {username}!", size=24, weight="bold", color='white'),
                # Adicione outros controles para a página inicial aqui
                ft.ElevatedButton(text="Logout", on_click=lambda e: switch_to_login(None))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    # Formulário de Login
    username_login = ft.TextField(label="Usuário", width=300)
    password_login = ft.TextField(label="Senha", width=300, password=True, can_reveal_password=True)
    login_button = ft.TextButton(text="Login", on_click=login_click)
    switch_to_signup_button = ft.TextButton(text="Não tem uma conta? Cadastre-se", on_click=switch_to_signup)
    
    login_form = ft.Column(
        controls=[
            ft.Text("Login", size=24, weight="bold", color='white'),
            username_login,
            password_login,
            login_button,
            switch_to_signup_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Formulário de Signup
    username_signup = ft.TextField(label="Usuário", width=300)
    password_signup = ft.TextField(label="Senha", width=300, password=True, can_reveal_password=True)
    signup_button = ft.TextButton(text="Cadastrar", on_click=signup_click)
    switch_to_login_button = ft.TextButton(text="Já tem uma conta? Faça login", on_click=switch_to_login)
    
    signup_form = ft.Column(
        controls=[
            ft.Text("Sign Up", size=24, weight="bold", color='white'),
            username_signup,
            password_signup,
            signup_button,
            switch_to_login_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Inicia com o formulário de login
    page.add(create_base_container(login_form))

if __name__ == "__main__":
    ft.app(target=main)