import flet as ft
import flet_audio as fta


def screen2Contenido(page:ft.Page):
    audio=fta.Audio(
        src="app/src/screens/audio.mp3",
        autoplay=False
    )

    page.services.append(audio)
    
    async def reproducir(e):
        await audio.play()

    async def pausar(e):
        await audio.pause()

    

    return ft.Column(
        controls=[
            ft.Text("Reproductor Musica"),
            ft.FilledButton(content="Reproducir", on_click=reproducir),
            ft.FilledButton(content="Pausar",on_click=pausar)
        ]
        

    )
        
    