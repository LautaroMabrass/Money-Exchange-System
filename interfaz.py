import flet as ft

def main(page: ft.Page):
    def compra(e):
        pass
    
    def venta(e):
        pass

    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text('Bienvenido ', size=70, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
    texto2 = ft.Text('Que operacion desea realizar: ', size=50, color=ft.Colors.BLACK)
    
    botones = [
        ft.FilledButton(
            text="Compra",
            on_click=compra,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=30)
            )
        ),
        ft.FilledButton(
            text="Venta",
            on_click=venta,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=30) 
            )
        )
    ]
    
    boton_fila = ft.Row(controls=botones, spacing=20, alignment=ft.MainAxisAlignment.CENTER)

    contenido = ft.Column(
        controls=[
            texto,
            ft.Container(padding=10),
            texto2,
            ft.Container(padding=10),  
            boton_fila
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(contenido)

ft.app(target=main)

