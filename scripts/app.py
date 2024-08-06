import flet as ft
from flet import *
import os
import cv2
import time
import pandas as pd

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
        if username == "" and password == "":
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

    def go_to_camera_page(e):
        page.controls.clear()
        page.add(create_base_container(camera_page()))
        page.update()

    def go_to_table_page(e):
        page.controls.clear()
        page.add(create_base_container(table_page()))
        page.update()

    def home_page(username):
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

    def camera_page():
        myimage = ft.Image(
            src=False,
            width=300,
            height=300,
            fit='cover'
        )

        def remove_all_photos():
            folder_path = "images/"
            files = os.listdir(folder_path)
            for file in files:
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"File successfully removed: {file_path}")
            page.update()

        def take_picture(e):
            remove_all_photos()
            cap = cv2.VideoCapture(0)
            cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Webcam", 400, 600)
            timestamp = str(int(time.time()))
            myfileface = f"myPhoto_{timestamp}.jpg"
            try:
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite(f"images/{myfileface}", frame)
                    cv2.putText(frame, "Capture successful!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    myimage.src = "images/" + myfileface
                    page.update()
                cap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                print(e)
                print("Error during capture")

        return ft.Column([
            ft.Text("Tire a foto da nota", size=30, weight="bold"),
            ft.ElevatedButton("Tirar foto", bgcolor="blue", color="white", on_click=take_picture),
            myimage,
            ft.ElevatedButton(text="Voltar para Home", on_click=lambda e: page.controls.clear() or page.add(create_base_container(home_page(""))))
        ])

    def table_page():
        df = pd.DataFrame({
            "test": ['1', "20", "40"],
            "test1": ['2', "21", "41"],
            "test2": ['3', "22", "43"],
        })

        def headers(df: pd.DataFrame) -> list:
            return [ft.DataColumn(ft.Text(header)) for header in df.columns]

        def rows(df: pd.DataFrame) -> list:
            rows = []
            for index, row in df.iterrows():
                rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(row[header])) for header in df.columns]))
            return rows

        datatable = ft.DataTable(
            columns=headers(df),
            rows=rows(df)
        )

        return ft.Column([
            ft.Text("Tabela de Dados", size=30, weight="bold"),
            datatable,
            ft.ElevatedButton(text="Voltar para Home", on_click=lambda e: page.controls.clear() or page.add(create_base_container(home_page(""))))
        ])

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
    ft.app(target=main, assets_dir='images')
