import flet as ft

def screen2Contenido(page:ft.Page):
    return ft.Column(
        controls=[
            ft.Text("Pantalla 2", size=30)
        ],
        expand=True
    )