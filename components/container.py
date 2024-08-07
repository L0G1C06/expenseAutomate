import flet as ft 

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
            controls=[
                content
            ]
        )
    )