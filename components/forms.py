import flet as ft

def create_login_form(login_click, switch_to_signup):
    username_login = ft.TextField(label="Usuário", width=300)
    password_login = ft.TextField(label="Senha", width=300, password=True, can_reveal_password=True)
    login_button = ft.TextButton(text="Login", on_click=lambda e: login_click(username_login, password_login))
    switch_to_signup_button = ft.TextButton(text="Não tem uma conta? Cadastre-se", on_click=switch_to_signup)

    return ft.Column(
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

def create_signup_form(signup_click, switch_to_login):
    username_signup = ft.TextField(label="Usuário", width=300)
    password_signup = ft.TextField(label="Senha", width=300, password=True, can_reveal_password=True)
    signup_button = ft.TextButton(text="Cadastrar", on_click=lambda e: signup_click(username_signup, password_signup))
    switch_to_login_button = ft.TextButton(text="Já tem uma conta? Faça login", on_click=switch_to_login)

    return ft.Column(
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