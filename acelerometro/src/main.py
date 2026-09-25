import flet as ft


def main(page: ft.Page):

    def obtenerLectura(evento:ft.AccelerometerReadingEvent):
        lectura.value=(
            f"x={evento.x:.2f}",
            f"y={evento.y:.2f}",
            f"z={evento.z:.2f}"
        )
        page.update()

    def controlError(evento:ft.SensorErrorEvent):
        page.add(
            ft.Text(f"Error al detectar el acelerometro {evento.message}")
        )
    page.services.append(ft.Accelerometer(
        on_reading=obtenerLectura,
        on_error=controlError,
        interval=ft.Duration(milliseconds=100),
        cancel_on_error=False
    ))
    
    page.add(
        ft.Text("Mueve el celular para obtener los datos"),
        lectura:= ft.Text("Esperando los datos...")
        
    )


ft.run(main)
