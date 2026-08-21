import flet as ft
import flet_video as ftv

from screens.screen1 import screen1Contenido
from screens.screen2 import screen2Contenido
from screens.screen3 import screen3Contenido
from screens.screen4 import screen4Contenido


def main(page: ft.Page):

    
    page.title = "Aplicaciones Móviles"

    page.appbar = ft.AppBar(
        title=ft.Text("Aplicaciones Móviles"),
        bgcolor="green"
    )

    
    selectId = 0

    
    contenido = ft.Container(
        expand=True
    )

    
    def cambiarPantalla(e):

        nonlocal selectId

        
        selectId = e.control.selected_index

        print("Pantalla seleccionada:", selectId)

        # Seleccionar contenido
        if selectId == 0:
            pantalla = screen1Contenido(page)

        elif selectId == 1:
            pantalla = screen2Contenido(page)

        elif selectId == 2:
            pantalla = screen3Contenido(page)

        elif selectId == 3:
            pantalla = screen4Contenido(page)

        # Cambiar contenido
        contenido.content = pantalla

        # Actualizar página
        page.update()

    
    navigation = ft.NavigationBar(
        selected_index=0,

        on_change=cambiarPantalla,

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
                label="Ubicación"
            )
        ],

        bgcolor="green"
    )

    contenido.content=screen1Contenido(page)
   
    

 
    page.add(
        contenido,
        navigation
    )


# EJECUTAR
ft.run(main)