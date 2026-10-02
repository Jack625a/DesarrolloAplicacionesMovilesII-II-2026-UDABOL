import flet as ft
import flet_lottie as ftl


def main(page: ft.Page):

    animacion = ftl.Lottie(
        src="https://lottie.host/19a8fa0f-ed94-4d4a-9f64-67f8168c92e7/2tfQpe616r.json",
        animate=True,
        height=200
    )
    animacion2=ftl.Lottie(
        src="https://lottie.host/6adb3c73-25eb-46e5-acd3-678514ce2e0a/IVIMp528tN.json",
        animate=True,
        height=600
    )


    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    animacion,
                    animacion2
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )


ft.run(main)