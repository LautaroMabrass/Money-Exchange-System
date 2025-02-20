import flet as ft
import sqlite3
import datetime

def operacion_venta(moneda_entregada, cantidad_entregada, moneda_recibida, tipo_de_cambio):
    cantidad_recibida = round(tipo_de_cambio * cantidad_entregada, 2)
    return cantidad_recibida

def operacion_compra(moneda_comprada, cantidad_comprada, moneda_vendida, tipo_de_cambio):
    cantidad_entregada = round(cantidad_comprada / tipo_de_cambio, 2)
    return cantidad_entregada

def cargar_datos(datos):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conexion = sqlite3.connect("base-casa-de-cambio.db")
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO transacciones(fecha, tipo_transaccion, moneda_origen, cantidad_origen, moneda_destino, cantidad_destino, tipo_cambio) VALUES(?, ?, ?, ?, ?, ?, ?)",
        (fecha_actual, 'compra', datos[0], datos[1], datos[2], datos[3], datos[4])
    )
    conexion.commit()
    conexion.close()

# Función principal
def main(page: ft.Page):
    def ir_a_compra(e):
        page.controls.clear()
        interfaz_compra(page)
        page.update()

    def ir_a_venta(e):
        page.controls.clear()
        interfaz_venta(page)
        page.update()

    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Casa de Cambio"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text('Bienvenido', size=60, color=ft.Colors.GREY_800, weight=ft.FontWeight.BOLD)
    texto2 = ft.Text('¿Qué operación desea realizar?', size=35, color=ft.Colors.GREY_800)

    botones = [
        ft.FilledButton(
            text="Compra",
            on_click=ir_a_compra,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.INDIGO_700,
                color=ft.Colors.WHITE,
                text_style=ft.TextStyle(size=24),
                shape=ft.RoundedRectangleBorder(radius=8)
            )
        ),
        ft.FilledButton(
            text="Venta",
            on_click=ir_a_venta,
            width=200,
            height=60,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.INDIGO_700,
                color=ft.Colors.WHITE,
                text_style=ft.TextStyle(size=24),
                shape=ft.RoundedRectangleBorder(radius=8)
            )
        )
    ]

    boton_fila = ft.Row(controls=botones, spacing=20, alignment=ft.MainAxisAlignment.CENTER)

    contenido = ft.Column(
        controls=[texto, ft.Container(padding=10), texto2, ft.Container(padding=10), boton_fila],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(contenido)

# Interfaz de venta
def interfaz_venta(page: ft.Page):
    def procesar_venta(moneda_vendida, cantidad_vendida, moneda_recibida, tipo_cambio):
        return operacion_venta(moneda_vendida, cantidad_vendida, moneda_recibida, tipo_cambio)

    def mostrar_snackbar(mensaje):
        snack_bar = ft.SnackBar(content=ft.Text(mensaje, color=ft.Colors.WHITE), bgcolor=ft.Colors.RED_700)
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    def ir_a_confirmacion(e):
        moneda_vendida = datos[0].value
        try:
            cantidad_vendida = float(datos[1].value)
        except ValueError:
            cantidad_vendida = None

        moneda_recibida = datos[2].value
        try:
            tipo_cambio = float(datos[3].value)
        except ValueError:
            tipo_cambio = None

        if not all([moneda_vendida, moneda_recibida]):
            mostrar_snackbar("Por favor, seleccione las monedas.")
            return

        if tipo_cambio is None or cantidad_vendida is None:
            mostrar_snackbar("Por favor, ingrese valores numéricos válidos.")
            return

        cantidad_recibida = procesar_venta(moneda_vendida, cantidad_vendida, moneda_recibida, tipo_cambio)
        page.controls.clear()
        interfaz_confirmar_venta(page, moneda_vendida, cantidad_vendida, moneda_recibida, tipo_cambio, cantidad_recibida)
        page.update()

    def retroceder(e):
        page.controls.clear()
        main(page)
        page.update()

    texto = ft.Text("Ingrese los siguientes datos para la VENTA:", size=45, color=ft.Colors.GREY_800, weight=ft.FontWeight.BOLD)

    boton_enviar = ft.FilledButton(
        text="Enviar",
        on_click=ir_a_confirmacion,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=180,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    opciones = [
        ft.Text("Moneda que se vendió:", size=24, color=ft.Colors.GREY_800),
        ft.Text("Cantidad de dinero que se vendió:", size=24, color=ft.Colors.GREY_800),
        ft.Text("Moneda que se recibió a cambio:", size=24, color=ft.Colors.GREY_800),
        ft.Text("Tipo de cambio:", size=24, color=ft.Colors.GREY_800),
    ]

    monedas = ["Dolar", "Pesos Argentinos", "Euros", "Chileno"]

    datos = [
        ft.Dropdown(
            label="Moneda Vendida",
            options=[ft.dropdown.Option(moneda) for moneda in monedas],
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        ),
        ft.TextField(
            label="Cantidad vendida",
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        ),
        ft.Dropdown(
            label="Moneda Recibida",
            options=[ft.dropdown.Option(moneda) for moneda in monedas],
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        ),
        ft.TextField(
            label="Tipo de cambio",
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        )
    ]

    columna_opciones = ft.Column(controls=opciones, spacing=30)
    columna_ingresos = ft.Column(controls=datos, spacing=30)

    fila_todos = ft.Row(controls=[columna_opciones, columna_ingresos], spacing=60, alignment=ft.MainAxisAlignment.CENTER)

    page.add(texto, ft.Container(height=30), fila_todos, ft.Container(height=30), boton_enviar, back_container)

# Interfaz de compra
def interfaz_compra(page: ft.Page):
    def procesar_compra(moneda_comprada, cantidad_comprada, moneda_vendida, tipo_cambio):
        return operacion_compra(moneda_comprada, cantidad_comprada, moneda_vendida, tipo_cambio)

    def mostrar_snackbar(mensaje):
        snack_bar = ft.SnackBar(content=ft.Text(mensaje, color=ft.Colors.WHITE), bgcolor=ft.Colors.RED_700)
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    def ir_a_confirmacion(e):
        moneda_comprada = datos[0].value
        try:
            cantidad_comprada = float(datos[1].value)
        except ValueError:
            cantidad_comprada = None

        moneda_vendida = datos[2].value
        try:
            tipo_cambio = float(datos[3].value)
        except ValueError:
            tipo_cambio = None

        if not all([moneda_comprada, moneda_vendida]):
            mostrar_snackbar("Por favor, seleccione las monedas.")
            return

        if tipo_cambio is None or cantidad_comprada is None:
            mostrar_snackbar("Por favor, ingrese valores numéricos válidos.")
            return

        cantidad_entregada = procesar_compra(moneda_comprada, cantidad_comprada, moneda_vendida, tipo_cambio)
        page.controls.clear()
        interfaz_confirmar_compra(page, moneda_comprada, cantidad_comprada, moneda_vendida, tipo_cambio, cantidad_entregada)
        page.update()

    def retroceder(e):
        page.controls.clear()
        main(page)
        page.update()

    texto = ft.Text("Ingrese los siguientes datos para la COMPRA:", size=45, color=ft.Colors.GREY_800, weight=ft.FontWeight.BOLD)

    boton_enviar = ft.FilledButton(
        text="Enviar",
        on_click=ir_a_confirmacion,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=180,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    opciones = [
        ft.Text("Moneda comprada:", size=24, color=ft.Colors.GREY_800),
        ft.Text("Cantidad de dinero que se compró:", size=24, color=ft.Colors.GREY_800),
        ft.Text("Moneda entregada a cambio:", size=24, color=ft.Colors.GREY_800),
        ft.Text("Tipo de cambio:", size=24, color=ft.Colors.GREY_800),
    ]

    monedas = ["Dolar", "Pesos Argentinos", "Euros", "Chileno"]

    datos = [
        ft.Dropdown(
            label="Moneda Comprada",
            options=[ft.dropdown.Option(moneda) for moneda in monedas],
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        ),
        ft.TextField(
            label="Cantidad comprada",
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        ),
        ft.Dropdown(
            label="Moneda Vendida",
            options=[ft.dropdown.Option(moneda) for moneda in monedas],
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        ),
        ft.TextField(
            label="Tipo de cambio",
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            focused_bgcolor=ft.Colors.INDIGO_50
        )
    ]

    columna_opciones = ft.Column(controls=opciones, spacing=30)
    columna_ingresos = ft.Column(controls=datos, spacing=30)

    fila_todos = ft.Row(controls=[columna_opciones, columna_ingresos], spacing=60, alignment=ft.MainAxisAlignment.CENTER)

    page.add(texto, ft.Container(height=30), fila_todos, ft.Container(height=30), boton_enviar, back_container)

# Confirmación de venta
def interfaz_confirmar_venta(page: ft.Page, moneda_vendida, cantidad_vendida, moneda_recibida, tipo_cambio, cantidad_recibida):
    def enviar(e):
        cargar_datos([moneda_vendida, cantidad_vendida, moneda_recibida, cantidad_recibida, tipo_cambio])
        page.controls.clear()
        main(page)
        page.update()

    def retroceder(e):
        page.controls.clear()
        interfaz_venta(page)

    texto = ft.Text("Confirme si los datos de la venta son correctos:", size=45, color=ft.Colors.GREY_800, weight=ft.FontWeight.BOLD)
    textos = [
        ft.Text(f"Moneda vendida: {moneda_vendida}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Cantidad vendida: {cantidad_vendida}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Moneda recibida: {moneda_recibida}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Tipo de cambio: {tipo_cambio}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Cantidad recibida: {cantidad_recibida}", size=24, color=ft.Colors.GREY_800)
    ]

    boton_confirmar = ft.FilledButton(
        text="Confirmar",
        on_click=enviar,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=180,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    page.add(texto, ft.Container(height=30), *textos, ft.Container(height=30), boton_confirmar, back_container)

# Confirmación de compra
def interfaz_confirmar_compra(page: ft.Page, moneda_comprada, cantidad_comprada, moneda_vendida, tipo_cambio, cantidad_entregada):
    def enviar(e):
        cargar_datos([moneda_comprada, cantidad_comprada, moneda_vendida, cantidad_entregada, tipo_cambio])
        page.controls.clear()
        main(page)
        page.update()

    def retroceder(e):
        page.controls.clear()
        interfaz_compra(page)

    texto = ft.Text("Confirme si los datos de la compra son correctos:", size=45, color=ft.Colors.GREY_800, weight=ft.FontWeight.BOLD)
    textos = [
        ft.Text(f"Moneda comprada: {moneda_comprada}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Cantidad comprada: {cantidad_comprada}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Moneda vendida: {moneda_vendida}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Tipo de cambio: {tipo_cambio}", size=24, color=ft.Colors.GREY_800),
        ft.Text(f"Cantidad entregada: {cantidad_entregada}", size=24, color=ft.Colors.GREY_800)
    ]

    boton_confirmar = ft.FilledButton(
        text="Confirmar",
        on_click=enviar,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
    boton_retroceder = ft.FilledButton(
        text="Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=180,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    back_container = ft.Container(content=boton_retroceder, alignment=ft.alignment.center_left)

    page.add(texto, ft.Container(height=30), *textos, ft.Container(height=30), boton_confirmar, back_container)

if __name__ == "__main__":
    ft.app(target=main)