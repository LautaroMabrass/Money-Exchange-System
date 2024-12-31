import flet as ft
class CajaInicial:
    def __init__(self, caja):
        self.caja = caja
    
    def operacion_venta(self, moneda_entregada, cantidad_entregada, moneda_recibida, tipo_de_cambio):
        dinero_total = tipo_de_cambio * cantidad_entregada
        return moneda_entregada, cantidad_entregada, moneda_recibida, dinero_total
    
    def operacion_compra(self, moneda_recibida, cantidad_comprada, moneda_entregada, tipo_de_cambio):
        cantidad_entregada = cantidad_comprada * tipo_de_cambio
        return moneda_recibida, cantidad_comprada, moneda_entregada, cantidad_entregada
    
    def cambio_caja_compra(self, datos):
        if datos[0] in self.caja:
            self.caja[datos[0]] += datos[1]
        if datos[2] in self.caja:
            self.caja[datos[2]] -= datos[3]
    
    def cambio_caja_venta(self, datos):
        if datos[0] in self.caja:
            self.caja[datos[0]] -= datos[1]
        if datos[2] in self.caja:
            self.caja[datos[2]] += datos[3]
        



# Interfaz principal
def main(page: ft.Page):
    caja_inicial = CajaInicial({"Dolar": 10000, "Euros": 10000, "Pesos Argentinos": 10000})
    def ir_a_compra(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_compra(page,caja_inicial)  # Cargar la interfaz de compra
        page.update()

    def ir_a_venta(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_venta(page, caja_inicial)  # Cargar la interfaz de venta
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
def interfaz_venta(page: ft.Page, caja_inicial):
    def venta(moneda_vendida,cantidad_vendida,moneda_recibida,tipo_cambio):
        caja_final = caja_inicial.operacion_venta(moneda_vendida,cantidad_vendida,moneda_recibida,tipo_cambio)
        caja_inicial.cambio_caja_venta(caja_final)
        return caja_final[3]
    def ir_a_confirmacion(e):
        # Obtener los valores de los inputs antes de continuar
        moneda_vendida = datos[0].value # Dropdown de moneda comprada
        try:
            cantidad_vendida = float(datos[1].value)  # Convertir cantidad comprada a int
        except ValueError:
            cantidad_vendida = None  # Si no es un número válido, lo dejamos como None o manejamos el error

        moneda_recibida = datos[2].value # Dropdown de moneda dada
        try:
            tipo_cambio = float(datos[3].value)  # Convertir tipo de cambio a int
        except ValueError:
            tipo_cambio = None  # Si no es un número válido, lo dejamos como None o manejamos el error
        if tipo_cambio and moneda_recibida and moneda_vendida and cantidad_vendida:
            cantidad_recibida = venta(moneda_vendida,cantidad_vendida,moneda_recibida,tipo_cambio)
            page.controls.clear()  # Limpiar los controles previos
            interfaz_confirmar_venta(page,moneda_vendida,cantidad_vendida,moneda_recibida,tipo_cambio,cantidad_recibida,caja_inicial)
            page.update()



        # Mostrar los valores en la consola (o procesarlos)
        print(f"Moneda comprada: {moneda_comprada}")
        print(f"Cantidad comprada: {cantidad_comprada}")
        print(f"Moneda dada: {moneda_dada}")
        print(f"Tipo de cambio: {tipo_cambio}")
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

    monedas = ["Dolar", "Peso Argentino", "Euro", "Chileno"]

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
def interfaz_compra(page: ft.Page, caja_inicial):
    def compra(moneda_comprada,cantidad_comprada,moneda_vendida,tipo_cambio):
        caja_final = caja_inicial.operacion_compra(moneda_comprada,cantidad_comprada,moneda_vendida,tipo_cambio)
        caja_inicial.cambio_caja_venta(caja_final)
        return caja_final[3]
    def ir_a_confirmacion(e):
        # Obtener los valores de los inputs antes de continuar
        moneda_comprada = datos[0].value  # Dropdown de moneda comprada
        try:
            cantidad_comprada = float(datos[1].value)  # Convertir cantidad comprada a int
        except ValueError:
            cantidad_comprada = None  # Si no es un número válido, lo dejamos como None o manejamos el error

        moneda_vendida = datos[2].value # Dropdown de moneda dada
        try:
            tipo_cambio = float(datos[3].value)  # Convertir tipo de cambio a int
        except ValueError:
            tipo_cambio = None  # Si no es un número válido, lo dejamos como None o manejamos el error
        if tipo_cambio and moneda_comprada and cantidad_comprada and moneda_vendida:
            cantidad_recibida = compra(moneda_comprada,cantidad_comprada,moneda_vendida,tipo_cambio)
            page.controls.clear()  # Limpiar los controles previos
            interfaz_confirmar_compra(page, moneda_comprada,cantidad_comprada,moneda_vendida,tipo_cambio,cantidad_recibida,caja_inicial)
            page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page,caja_inicial)
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

    monedas = ["Dolar", "Peso Argentino", "Euro", "Chileno"]

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

#Interfaz confirmar venta
def interfaz_confirmar_venta(page: ft.Page,moneda_vendida,cantidad_vendida,moneda_recibida,tipo_cambio,cantidad_recibida,caja_inicial):
    def enviar(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page)
        page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_venta(page,caja_inicial)

    # Configuración de la página
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    texto = ft.Text("Confirme si son correctos los siguientes datos:", size=50, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
    # moneda_vendida,cantidad_vendida,moneda_recibida,tipo_cambio,cantidad_recibida
    # Texto informativo para cada campo
    textos = [
        ft.Text(f"Moneda vendida: {moneda_vendida}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Cantidad vendida: {cantidad_vendida}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Moneda recibida: {moneda_recibida}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Tipo de cambio: {tipo_cambio}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Cantidad recibida: {cantidad_recibida}", size=30, color=ft.Colors.BLACK)
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

#interfaz_confirmar_venta
def interfaz_confirmar_compra(page: ft.Page, moneda_comprada,cantidad_comprada,moneda_vendida,tipo_cambio,cantidad_recibida,caja_inicial):
    def enviar(e):
        page.controls.clear()  # Limpiar los controles previos
        main(page)
        page.update()

    def retroceder(e):
        page.controls.clear()  # Limpiar los controles previos
        interfaz_compra(page,caja_inicial)

    # Configuración de la página
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de cambio sistema"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título principal
    texto = ft.Text("Confirme si son correctos los siguientes datos:", size=50, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

    # Texto informativo para cada campo
    textos = [
        ft.Text(f"Moneda comprada: {moneda_comprada}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Cantidad comprada: {cantidad_comprada}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Moneda entregada a cambio: {moneda_vendida}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Tipo de cambio: {tipo_cambio}", size=30, color=ft.Colors.BLACK),
        ft.Text(f"Cantidad dada: {cantidad_recibida}", size=30, color=ft.Colors.BLACK)
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
