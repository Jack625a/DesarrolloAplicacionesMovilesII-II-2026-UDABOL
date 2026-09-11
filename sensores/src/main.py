import flet as ft
from flet_geolocator import Geolocator


async def main(page: ft.Page):
    page.appbar=ft.AppBar(title="Geolocalizacion")
    geolocalizacion=Geolocator()
    page.services.append(geolocalizacion)

    resultado=ft.Text("Presiona el boton para obtener la ubicacion")

    async def obtenerCoordenadas(e):
        resultado.value="Detectando la ubicación..."
        page.update()
        try: 
            servicioActivo=await geolocalizacion.is_location_service_enabled()
            if not servicioActivo:
                resultado.value="Activa tu gps..."
                page.update()
                return
            posicion=await geolocalizacion.get_current_position()
            resultado.value=(
                f"Latidud: {posicion.latitude}\n"
                f"Longitud: {posicion.longitude}"
            )
            print(f"Latitud {posicion.latitude} - Longitud {posicion.longitude}")
        except Exception as error:
            resultado.valu="Error al obetener su ubicacion" \
              
    page.add(
        ft.Button("Obtener Ubicacion",icon=ft.Icons.GPS_FIXED,on_click=obtenerCoordenadas),
        resultado
    )


if __name__ == "__main__":
    ft.run(main)
