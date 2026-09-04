import flet as ft
import flet_camera as fc

async def main(page: ft.Page):
    page.title = "Cámara Simple"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 1. Widget principal de la cámara
    camara = fc.Camera(
        expand=True,
        preview_enabled=True,
    )

    # 2. Selector de cámara
    selector_camara = ft.Dropdown(label="Selecciona una cámara", width=300)

    # Función para cargar las cámaras disponibles al iniciar
    async def cargar_camaras(e=None):
        camaras_disponibles = await camara.get_available_cameras()
        selector_camara.options = [
            ft.DropdownOption(key=c.name, text=c.name) for c in camaras_disponibles
        ]
        page.update()

    # Función para encender la cámara seleccionada
    async def activar_camara(e):
        if not selector_camara.value:
            return
        
        # Buscar los detalles de la cámara seleccionada
        camaras_disponibles = await camara.get_available_cameras()
        camara_seleccionada = next(
            (c for c in camaras_disponibles if c.name == selector_camara.value), 
            None
        )

        if camara_seleccionada:
            # Inicializar y mostrar la imagen
            await camara.initialize(
                description=camara_seleccionada,
                resolution_preset=fc.ResolutionPreset.MEDIUM
            )
            page.update()

    # Asignar eventos
    selector_camara.on_change = activar_camara
    page.on_connect = cargar_camaras

    # 3. Construir la interfaz
    page.add(
        ft.Row(
            [selector_camara, ft.IconButton(ft.Icons.REFRESH, on_click=cargar_camaras)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Container(
            content=camara,
            width=640,
            height=480,
            bgcolor=ft.Colors.BLACK,
            border_radius=10,
        )
    )

    # Ejecutar la carga de cámaras al abrir
    await cargar_camaras()

if __name__ == "__main__":
    ft.run(main)