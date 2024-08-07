import flet as ft

def home_page(username, go_to_camera_page, go_to_table_page, switch_to_login):
    return ft.Column(
        controls=[
            ft.Text(f"Olá {username}!", size=24, weight="bold", color='white'),
            ft.ElevatedButton(text="Tirar foto", on_click=go_to_camera_page),
            ft.ElevatedButton(text="Ver Tabela", on_click=go_to_table_page),
            ft.ElevatedButton(text="Logout", on_click=switch_to_login)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )