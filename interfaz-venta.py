import flet as ft

def main(page: ft.Page):
    def enviar(e):
        pass
    # Configuración de la página
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    texto = ft.Text(
        "Ingrese lo siguientes datos correspondientes:", 
        size=50, 
        color=ft.Colors.BLACK,
        weight=ft.FontWeight.BOLD
    )
    botonEnviar = ft.FilledButton(
            text="Enviar",
            on_click=enviar,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=30)
            )
        )
    # Textos descriptivos
    opciones = [
        ft.Text("Ingrese la moneda que se vendió:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese la cantidad de dinero que se vendió:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese la moneda que se recibió a cambio:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese el tipo de cambio:", size=30, color=ft.Colors.BLACK),
    ]

    # Opciones de entrada
    monedas = ["Dólar", "Peso Argentino", "Euro", "Chileno"]

    datos = [
        ft.Dropdown(
            label="Opciones", 
            options=[ft.dropdown.Option(moneda) for moneda in monedas], 
            border_radius=8
        ),
        ft.TextField(label="Cantidad vendida", border_radius=8),
        ft.Dropdown(
            label="Opciones", 
            options=[ft.dropdown.Option(moneda) for moneda in monedas], 
            border_radius=8
        ),
        ft.TextField(label="Tipo de cambio", border_radius=8)
    ]

    # Columnas
    columna_opciones = ft.Column(
        controls=opciones,
        spacing=40
    )

    columna_ingresos = ft.Column(
        controls=datos,
        spacing=40
    )

    # Fila que contiene las columnas
    fila_todos = ft.Row(
        controls=[columna_opciones, columna_ingresos],
        spacing=60,  # Espaciado entre las columnas
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Separación entre el texto principal y el formulario
    separador = ft.Container(height=30)  # Espacio vacío de 30 píxeles

    # Agregar elementos a la página
    page.add(texto, separador, fila_todos, separador, botonEnviar)

ft.app(target=main)

