import flet as ft #Importacion
import flet_video as ftv

from screens.screen1 import screen1Contenido
from screens.screen2 import screen2Contenido
from screens.screen3 import screen3Contenido
from screens.screen4 import screen4Contenido


def main(page: ft.Page): #Funcion Principal

    page.appbar=ft.AppBar(title="Aplicaciones Moviles",bgcolor="green")

    selectId=0

    contenido=ft.Container(expand=True)

    def cambiarPantalla(e):
        nonlocal selectId
        selectId=e.control.selected_index
        if selectId==0:
            pantalla=screen1Contenido(page)
        elif selectId==1:
            pantalla=screen2Contenido(page)
        elif selectId==2:
            pantalla=screen3Contenido(page)
        elif selectId==3:
            pantalla=screen4Contenido(page)

        contenido.content=pantalla
        page.update()

    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME, 
                label="Inicio"
                ),
            ft.NavigationBarDestination(
                icon=ft.Icons.TIKTOK,
                label="Redes"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.FACE,
                label="Perfil"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.GPS_FIXED,
                label="Ubicacion"
            )
        ],
        bgcolor="green"
    )
    
    page.add( #Interfaz
        contenido
       
    )


ft.run(main) #Ejecución
