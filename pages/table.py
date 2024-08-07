import flet as ft
import pandas as pd

from .home import home_page
from components.container import create_base_container

def table_page(page, go_to_camera_page, go_to_table_page, switch_to_login):
    df = pd.read_excel('./planilhas/planilhaDevelopment.xlsx')

    def headers(df: pd.DataFrame) -> list:
        return [ft.DataColumn(ft.Text(header)) for header in df.columns]

    def rows(df: pd.DataFrame) -> list:
        rows = []
        for index, row in df.iterrows():
            rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(str(row[header]))) for header in df.columns]))
        return rows

    datatable = ft.DataTable(
        columns=headers(df),
        rows=rows(df),
        divider_thickness=5,
        column_spacing=20
    )

    horizontal_scroll = ft.Row(
        controls=[
            ft.Column(
                controls=[datatable],
                scroll=ft.ScrollMode.ALWAYS
            )
        ],
        scroll=ft.ScrollMode.ALWAYS
    )

    vertical_scroll = ft.Column(
        controls=[
            horizontal_scroll,
            ft.ElevatedButton(
                text="Voltar para Home Page",
                on_click=lambda e: page.controls.clear() or page.add(create_base_container(home_page("", go_to_camera_page=go_to_camera_page, go_to_table_page=go_to_table_page, switch_to_login=switch_to_login)))
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )

    return ft.Container(
        content=vertical_scroll,
        height=600,
        width=500
    )
