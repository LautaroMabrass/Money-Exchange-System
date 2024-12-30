import flet as ft

# Interfaz principal
def main(page: ft.Page):
    def ir_a_compra(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_compra(page)  # Cargar la interfaz de compra
        page.update()

    def ir_a_venta(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_venta(page)  # Cargar la interfaz de venta
        page.update()

    # Configuración de la página
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Texto de bienvenida
    texto = ft.Text('Bienvenido', size=70, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
    texto2 = ft.Text('¿Qué operación desea realizar?', size=50, color=ft.Colors.BLACK)

    # Botones de Compra y Venta
    botones = [
        ft.FilledButton(
            text="Compra",
            on_click=ir_a_compra,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=30)
            )
        ),
        ft.FilledButton(
            text="Venta",
            on_click=ir_a_venta,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                text_style=ft.TextStyle(size=30)
            )
        )
    ]

    # Fila de botones
    boton_fila = ft.Row(controls=botones, spacing=20, alignment=ft.MainAxisAlignment.CENTER)

    # Contenido de la página
    contenido = ft.Column(
        controls=[texto, ft.Container(padding=10), texto2, ft.Container(padding=10), boton_fila],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Agregar el contenido a la página
    page.add(contenido)

# Interfaz venta
def interfaz_venta(page: ft.Page):
    def ir_a_confirmacion(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_confirmar_venta(page)
        page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page)
        page.update()

    # Configuración de la página
    texto = ft.Text("Ingrese los siguientes datos correspondientes sobre la VENTA:", size=50, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    # Botones
    boton_enviar = ft.FilledButton(
        text="Enviar",
        on_click=ir_a_confirmacion,
        width=200,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )

    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        on_click=retroceder,
        width=150,
        height=50,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20))
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    # Controles de la interfaz
    opciones = [
        ft.Text("Ingrese la moneda que se vendió:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese la cantidad de dinero que se vendió:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese la moneda que se recibió a cambio:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese el tipo de cambio:", size=30, color=ft.Colors.BLACK),
    ]

    monedas = ["Dólar", "Peso Argentino", "Euro", "Chileno"]

    datos = [
        ft.Dropdown(label="Opciones", options=[ft.dropdown.Option(moneda) for moneda in monedas], border_radius=8),
        ft.TextField(label="Cantidad vendida", border_radius=8),
        ft.Dropdown(label="Opciones", options=[ft.dropdown.Option(moneda) for moneda in monedas], border_radius=8),
        ft.TextField(label="Tipo de cambio", border_radius=8)
    ]

    # Columnas
    columna_opciones = ft.Column(controls=opciones, spacing=40)
    columna_ingresos = ft.Column(controls=datos, spacing=40)

    fila_todos = ft.Row(
        controls=[columna_opciones, columna_ingresos],
        spacing=60,  # Espaciado entre las columnas
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Añadir elementos a la página
    page.add(texto, ft.Container(height=30), fila_todos, ft.Container(height=30), boton_enviar, back_container)

# Interfaz compra
def interfaz_compra(page: ft.Page):
    def ir_a_confirmacion(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_confirmar_compra(page)
        page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page)
        page.update()

    # Configuración de la página
    texto = ft.Text("Ingrese los siguientes datos correspondientes sobre la COMPRA:", size=50, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    # Botones
    boton_enviar = ft.FilledButton(
        text="Enviar",
        on_click=ir_a_confirmacion,
        width=200,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )

    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        on_click=retroceder,
        width=150,
        height=50,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20))
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    # Controles de la interfaz
    opciones = [
        ft.Text("Ingrese la moneda que se compró:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese la cantidad de dinero que se compró:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese la moneda que se dio a cambio:", size=30, color=ft.Colors.BLACK),
        ft.Text("Ingrese el tipo de cambio:", size=30, color=ft.Colors.BLACK),
    ]

    monedas = ["Dólar", "Peso Argentino", "Euro", "Chileno"]

    datos = [
        ft.Dropdown(label="Opciones", options=[ft.dropdown.Option(moneda) for moneda in monedas], border_radius=8),
        ft.TextField(label="Cantidad comprada", border_radius=8),
        ft.Dropdown(label="Opciones", options=[ft.dropdown.Option(moneda) for moneda in monedas], border_radius=8),
        ft.TextField(label="Tipo de cambio", border_radius=8)
    ]

    # Columnas
    columna_opciones = ft.Column(controls=opciones, spacing=40)
    columna_ingresos = ft.Column(controls=datos, spacing=40)

    fila_todos = ft.Row(
        controls=[columna_opciones, columna_ingresos],
        spacing=60,  # Espaciado entre las columnas
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Añadir elementos a la página
    page.add(texto, ft.Container(height=30), fila_todos, ft.Container(height=30), boton_enviar, back_container)

def interfaz_confirmar_venta(page: ft.Page):
    def enviar(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page)
        page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_venta(page)

    # Configuración de la página
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    texto = ft.Text("Confirme si son correctos los siguientes datos:", size=50, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    # Texto informativo para cada campo
    textos = [
        ft.Text("Moneda vendida:", size=30, color=ft.Colors.BLACK),
        ft.Text("Cantidad vendida:", size=30, color=ft.Colors.BLACK),
        ft.Text("Moneda recibida:", size=30, color=ft.Colors.BLACK),
        ft.Text("Tipo de cambio:", size=30, color=ft.Colors.BLACK),
        ft.Text("Cantidad recibida:", size=30, color=ft.Colors.BLACK)
    ]

    # Botón de confirmación
    botonConfirmar = ft.FilledButton(
        text="Confirmar",
        on_click=enviar,
        width=200,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )

    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        on_click=retroceder,
        width=150,
        height=50,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20))
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    # Estructura de la columna, agregando texto y botón
    textos_columnas = ft.Column(
        controls=[texto] + textos + [botonConfirmar],        
        spacing=30,  # Espaciado entre los controles
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Añadir la columna a la página
    page.add(textos_columnas,back_container)

def interfaz_confirmar_compra(page: ft.Page):
    def enviar(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page)
        page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_compra(page)

    # Configuración de la página
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    texto = ft.Text("Confirme si son correctos los siguientes datos:", size=50, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    # Texto informativo para cada campo
    textos = [
        ft.Text("Moneda comprada:", size=30, color=ft.Colors.BLACK),
        ft.Text("Cantidad comprada:", size=30, color=ft.Colors.BLACK),
        ft.Text("Moneda recibida:", size=30, color=ft.Colors.BLACK),
        ft.Text("Tipo de cambio:", size=30, color=ft.Colors.BLACK),
        ft.Text("Cantidad dada:", size=30, color=ft.Colors.BLACK)
    ]

    # Botón de confirmación
    botonConfirmar = ft.FilledButton(
        text="Confirmar",
        on_click=enviar,
        width=200,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )

    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        on_click=retroceder,
        width=150,
        height=50,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=20))
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    # Estructura de la columna, agregando texto y botón
    textos_columnas = ft.Column(
        controls=[texto] + textos + [botonConfirmar],        
        spacing=30,  # Espaciado entre los controles
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Añadir la columna a la página
    page.add(textos_columnas,back_container)

ft.app(target=main)
