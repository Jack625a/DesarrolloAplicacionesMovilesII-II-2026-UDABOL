import flet as ft
import flet_map as map
from flet_geolocator import Geolocator

async def main(page: ft.Page):

    #Paso1. Configurar Geolocalizacion
    geolocalizacion=Geolocator()

    page.services.append(geolocalizacion)

    resultado=ft.Text("Obten la ubicacion dando click en el boton")
    #Paso 2. Crear los marcadores
    marcadores=map.MarkerLayer(
        markers=[]
    )
    #Paso3. Crear el mapa
    mapa=map.Map(
        expand=True,
        initial_center=map.MapLatitudeLongitude(
            -17.9604176,
            -67.1106498
        ),
        initial_zoom=15,
        layers=[
            #Mapa Google Maps
            map.TileLayer(
                url_template=(
                    "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
                )
            ),
            marcadores
        ]
    )

    #Paso 4. Funcion para obtener la ubicacion
    async def obtenerUbicacion(e):
        resultado.value="Obteniendo Ubicacion..."
        page.update()

        try:
            #verificacion del GPS
            activo=await (geolocalizacion.is_location_service_enabled()
            )
            if not activo:
                resultado.value="Activa tu gps"
                page.update()
                return
            posicion=await (geolocalizacion.get_current_position())

            latitud=posicion.latitude
            longitud=posicion.longitude

            print(latitud,"-",longitud)

            resultado.value=(
                f"Latitud: {latitud} - Longitud: {longitud}"
            )
            marcadores.markers.clear()
            marcador=map.Marker(
                coordinates=map.MapLatitudeLongitude(
                    latitud,
                    longitud
                ),
                content=ft.Icon(ft.Icons.LOCATION_ON, color="red",size=60)
            )
            marcadores.markers.append(marcador)
            mapa.initial_center=(
                map.MapLatitudeLongitude(
                    latitud,
                    longitud
                )
            )
            mapa.initial_zoom=18
            page.update()
        except Exception as error:
            resultado.value=f"Error al obtener los datos {error}"
            page.update()

    boton=ft.Button("Obtener Ubicacion", on_click=obtenerUbicacion)


    page.add(
        boton,
        resultado,
        mapa
    )


ft.run(main)
