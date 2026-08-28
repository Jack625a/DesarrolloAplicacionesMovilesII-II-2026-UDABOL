import flet as ft
import flet_camera as ftc

async def screen3Contenido(page:ft.Page):

    camara=ftc.Camera(
        expand=True,
        preview_enabled=True
    )
    page.add(camara)

   
    camaras=await camara.get_available_cameras()
    print(camaras)

    if camaras:
        await camara.initialize(
            description=camaras[0],
            resolucion=ftc.ResolutionPreset.MEDIUM
        )
   

    async def foto(e):
        imagen=camara.take_picture()
        print(f"Foto Tomanda : {imagen}")

    return ft.Column(
        controls=[
            ft.Text("Activacion Camara", size=30),
            ft.FilledButton("Sacar Foto", on_click=foto)
        ],
        expand=True
    )