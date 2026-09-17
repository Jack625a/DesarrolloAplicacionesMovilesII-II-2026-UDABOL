import flet as ft
import flet_map as map
from flet_geolocator import Geolocator


async def main(page: ft.Page):

   
    page.title = "Geolocalización"

    
    geolocalizacion = Geolocator()
    page.services.append(geolocalizacion)

   
    resultado = ft.Text(
        "Presiona el botón para obtener la ubicación"
    )

    
    marcadores = map.MarkerLayer(
        markers=[]
    )

  
    mapa = map.Map(
        expand=True,
        initial_center=map.MapLatitudeLongitude(
            -17.960510638,
            -67.110656400
        ),

        initial_zoom=15,

        layers=[
            
            map.TileLayer(
                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
            ),

           
            marcadores
        ]
    )

    
    async def obtenerCoordenadas(e):

        resultado.value = "Detectando la ubicación..."
        page.update()

        try:

            
            servicioActivo = await geolocalizacion.is_location_service_enabled()

            if not servicioActivo:

                resultado.value = "Activa el GPS o servicio de ubicación."

                page.update()

                return

            posicion = await geolocalizacion.get_current_position()
            latitud = posicion.latitude
            longitud = posicion.longitude
            
         
            resultado.value = (
                f"Latitud: {posicion.latitude}\n"
                f"Longitud: {posicion.longitude}"
            )

            print(
                f"Latitud: {latitud} - Longitud: {longitud}"
            )

            
            marcadores.markers.clear()

           
            marcador = map.Marker(
                coordinates=map.MapLatitudeLongitude(
                    posicion.latitude,
                    posicion.longitude
                ),
                content=ft.Icon(ft.Icons.LOCATION_ON, color="red",size=80)
            
            )

     
            marcadores.markers.append(marcador)

            
            mapa.initial_center = map.MapLatitudeLongitude(
                posicion.latitude,
                posicion.longitude
            )

          
            mapa.initial_zoom = 15

            
            page.update()

        except Exception as error:

            print("Error:", error)

            resultado.value = (
                f"Error al obtener la ubicación:\n{error}"
            )

            page.update()

  
    boton = ft.Button(
        "Obtener Ubicación",
        icon=ft.Icons.GPS_FIXED,
        on_click=obtenerCoordenadas
    )

  
    page.add(
        boton,
        resultado,
        mapa
    )



if __name__ == "__main__":

    ft.run(main)

