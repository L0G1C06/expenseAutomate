import flet as ft
import pandas as pd

# Carrega os dados do arquivo Excel
df = pd.read_excel('/home/weber/projects/expenseAutomate/scripts/planilhas/planilha2023.xlsx')

def headers(df: pd.DataFrame) -> list:
    return [ft.DataColumn(ft.Text(header)) for header in df.columns]

def rows(df: pd.DataFrame) -> list:
    rows = []
    for index, row in df.iterrows():
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(str(row[header]))) for header in df.columns]))
    return rows

def main(page: ft.Page):

    # Criação da DataTable
    datatable = ft.DataTable(
        columns=headers(df),
        rows=rows(df),
        divider_thickness=5,
        column_spacing=20
    )

    # Criação de uma Container para rolagem horizontal
    horizontal_scroll = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    datatable
                ],
                scroll=ft.ScrollMode.ALWAYS
            )
        ],
        scroll=ft.ScrollMode.ALWAYS
    )

    # Criação de uma Container para rolagem vertical
    vertical_scroll = ft.Column(
        controls=[
            horizontal_scroll
        ],
        scroll=ft.ScrollMode.ALWAYS
    )

    page.add(
        ft.Container(
            content=vertical_scroll,
            border=ft.border.all(1),
            height=600,  # ajuste a altura conforme necessário
            width=500    # ajuste a largura conforme necessário
        )
    )

ft.app(target=main)
