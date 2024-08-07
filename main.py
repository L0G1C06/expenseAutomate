import flet as ft

from pages.home import home_page
from pages.camera import camera_page
from pages.table import table_page
from components.forms import create_login_form, create_signup_form
from components.container import create_base_container

def main(page: ft.Page):
    page.title = "Expense Automate App"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    def login_click(username_login, password_login):
        username = username_login.value
        password = password_login.value
        if username == "" and password == "":
            page.controls.clear()
            page.add(create_base_container(home_page(username, go_to_camera_page, go_to_table_page, switch_to_login)))
        else:
            page.add(ft.Text("Usuário ou senha incorretos. Tente novamente!", color='red'))
        page.update()

    def signup_click(username_signup, password_signup):
        username = username_signup.value
        password = password_signup.value
        if username == "" or password == "":
            page.add(ft.Text("Todos os campos devem ser preenchidos", color='red'))
        else:
            page.add(ft.Text(f"Usuário {username} registrado com sucesso!", color='green'))
        page.update()

    def switch_to_login(e):
        page.controls.clear()
        page.add(create_base_container(create_login_form(login_click, switch_to_signup)))
        page.update()

    def switch_to_signup(e):
        page.controls.clear()
        page.add(create_base_container(create_signup_form(signup_click, switch_to_login)))
        page.update()

    def go_to_camera_page(e):
        page.controls.clear()
        page.add(create_base_container(camera_page(page, home_page, go_to_camera_page=go_to_camera_page, go_to_table_page=go_to_table_page, switch_to_login=switch_to_login)))
        page.update()

    def go_to_table_page(e):
        page.controls.clear()
        page.add(create_base_container(table_page(page=page, go_to_camera_page=go_to_camera_page, go_to_table_page=go_to_table_page, switch_to_login=switch_to_login)))
        page.update()

    # Inicia com o formulário de login
    page.add(create_base_container(create_login_form(login_click, switch_to_signup)))

if __name__ == "__main__":
    ft.app(target=main, assets_dir='images')