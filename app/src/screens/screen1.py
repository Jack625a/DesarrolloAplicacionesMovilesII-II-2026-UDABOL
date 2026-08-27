import flet as ft
import flet_video as ftv


def screen1Contenido(page: ft.Page):

    video = ftv.Video(
        playlist=[
            ftv.VideoMedia(
                "https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4"
            ),
            ftv.VideoMedia(
                "https://res.cloudinary.com/dw0d6ieuf/video/upload/v1787346675/Sabes_qu%C3%A9_es_PYTHON_y_por_qu%C3%A9_es_un_lenguaje_de_programaci%C3%B3n_tan_importante__vkjvnx.mp4"
            ),
        ],
        autoplay=False,
        show_controls=True,
        expand=True,
    )

    return ft.Column(
        controls=[
            ft.Text(
                "Reproductor de Video",
                size=25,
                weight=ft.FontWeight.BOLD,
            ),

            ft.Container(
                content=video,
                expand=True,
            ),
        ],
        expand=True,
        spacing=10,
    )