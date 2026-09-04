import flet as ft
import flet_camera as fc


async def screen3Contenido(page: ft.Page):

    camara = fc.Camera(
        expand=True,
        preview_enabled=True
    )

    seleccionarCamara=ft.Dropdown(label="Seleccione la Camara",width=300)
    

    estado = ft.Text("Buscando cámara...")

    async def cargarCamaras(e:None):
        # Obtener cámaras
        camarasDisponibles = await camara.get_available_cameras()
        seleccionarCamara.options=[
            ft.DropdownOption(key=c.name, text=c.name) for c in camarasDisponibles
        ]
        page.update()

    async def activarCamara(e):
        if not seleccionarCamara.value:
            return
        camarasDisponibles= await camara.get_available_cameras()
        camaraSeleccionada=next((c for c in camarasDisponibles if c.name==seleccionarCamara.value),None)

        if camaraSeleccionada:
            # Inicializar primera cámara
            await camara.initialize(
                description=camaraSeleccionada,
                resolution_preset=fc.ResolutionPreset.MEDIUM,
                #enable_audio=False,
                #image_format_group=fc.ImageFormatGroup.JPEG
            )
            page.update()

        seleccionarCamara.on_change=activarCamara
        page.on_connect=cargarCamaras
        
    
    page.add(
        ft.Row(
        [seleccionarCamara,
            ft.CupertinoFilledButton("Activar",on_click=cargarCamaras)
        ]),
        ft.Container(
            content=camara,
            width=600,
            height=400,
            border_radius=10
        )
    )
    await cargarCamaras()

if __name__=="__main__":
    ft.run(screen3Contenido)