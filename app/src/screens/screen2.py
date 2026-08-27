import flet as ft
import flet_audio as fta


def screen2Contenido(page:ft.Page):
    


    audio=fta.Audio(
        src="https://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3",
        autoplay=True
    )

    async def reproducir():
        await audio.play()

    async def pausar():
        await audio.pause()

    

    return ft.Column(
        controls=[
            ft.Text("Reproductor Musica"),
            ft.FilledButton(content="Reproducir", on_click=reproducir),
            ft.FilledButton(content="Pausar",on_click=pausar)
        ]
        

    )
        
    