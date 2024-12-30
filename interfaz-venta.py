import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text("Ingrese lo siguientes datos correspondientes: ",size=50, color=ft.Colors.BLACK)

    opciones = [ft.Text("Ingrese la moneda que se vendio: ",size=30, color=ft.Colors.BLACK),
    ft.Text("Ingrese la cantidad de dinero que se vendio: ",size=30, color=ft.Colors.BLACK),
    ft.Text("Ingrese el tipo de cambio: ",size=30, color=ft.Colors.BLACK),
    ft.Text("Ingrese la moneda que se recibio: ",size=30, color=ft.Colors.BLACK)]

    monedas = ["Dolar","Peso Argentino","Euro","Chileno"]

    datos = [ft.Dropdown(label="Opciones",options=[ft.dropdown.Option(moneda) for moneda in monedas],border_radius=8),ft.Dropdown(label="Opciones",options=[ft.dropdown.Option(moneda) for moneda in monedas],border_radius=8),ft.TextField(label="Cantidad entregada", border_radius=8),ft.TextField(label="Tipo de cambio", border_radius=8)]

    columna_opciones = ft.Column(
        controls = opciones,spacing=20
    )

    columna_ingresos = ft.Column(
        controls=datos,spacing=20
    )

    fila_todos = ft.Row(
        controls=[columna_opciones,columna_ingresos], spacing=5
    )

    page.add(texto,fila_todos)

ft.app(target=main)