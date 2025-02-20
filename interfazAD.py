import flet as ft
import sqlite3

def main(page: ft.Page):
    # Fondo de la página más suave y profesional
    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Casa de Cambio"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def ir_transac(e):
        page.controls.clear()
        transac(page)
        page.update() 
    
    def ir_caja(e):
        page.controls.clear()
        caja(page)
        page.update() 

    # Texto principal ajustado en tamaño y color
    texto = ft.Text(
        "Bienvenido, ¿qué deseas hacer hoy?",
        size=60,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    # Botones con estilo moderno y compacto
    transacciones = ft.FilledButton(
        "Transacciones",
        on_click=ir_transac,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )
    cajas = ft.FilledButton(
        "Caja",
        on_click=ir_caja,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    # Contenido con mayor espaciado para una mejor distribución
    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([transacciones, cajas], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ],
        spacing=30
    )

    page.add(contenido)

# Interfaz de Caja
def caja(page: ft.Page):

    def refrescarData(e):
        pass

    def retroceder(e):
        page.controls.clear()
        main(page)
        page.update() 

    # Fondo consistente con la pantalla principal
    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Casa de Cambio - Caja"  # Corregido el título
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Texto más proporcionado
    texto = ft.Text(
        "Caja actual",
        size=45,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
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

    recargar = ft.FilledButton(
        "Recargar",
        on_click=refrescarData,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    # Contenido con espaciado mejorado
    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([recargar], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([boton_retroceder], alignment=ft.MainAxisAlignment.START)
        ],
        spacing=30
    )

    page.add(contenido)

# Interfaz de transacciones
def transac(page: ft.Page):
    def retroceder(e):
        page.controls.clear()
        main(page)
        page.update() 

    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Casa de Cambio - Transacciones"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    texto = ft.Text(
        "Transacciones",
        size=45,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    data_table = ft.DataTable(
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.GREY_400),
        border_radius=5,
        vertical_lines=ft.border.BorderSide(1, ft.Colors.GREY_400),
        horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREY_400),
        columns=[
            ft.DataColumn(ft.Text("FECHA", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("TIPO DE TRANSACCION", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("MONEDA ORIGEN", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("CANTIDAD ORIGEN", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("MONEDA DESTINO", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("CANTIDAD DESTINO", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("TIPO DE CAMBIO", color=ft.Colors.BLACK, size=18))
        ],
        rows=[],
        heading_row_color=ft.Colors.INDIGO_100,
        data_row_color={"": ft.Colors.WHITE, "hovered": ft.Colors.INDIGO_50},
    )
    tabla_row = ft.Row(
        controls=[data_table],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    tabla_column = ft.Column(
        controls=[tabla_row],
        scroll=ft.ScrollMode.AUTO,  
        expand=True
    )

    tabla_container = ft.Container(
        content=tabla_column,
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=2, color=ft.Colors.GREY_400),
        border_radius=5,
        padding=20, 
        width=page.width - 40,  
        height=400,
        bgcolor=ft.Colors.WHITE 
    )
    def refrescarData(e):
        conexion = sqlite3.connect("base-casa-de-cambio.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM transacciones")
        filas = cursor.fetchall()
        conexion.close()
        data_table.rows.clear()
        for fila in filas:
            nueva_fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(fila[0], color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                    ft.DataCell(ft.Text(fila[1], color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                    ft.DataCell(ft.Text(fila[2], color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                    ft.DataCell(ft.Text(str(fila[3]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                    ft.DataCell(ft.Text(fila[4], color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                    ft.DataCell(ft.Text(str(fila[5]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                    ft.DataCell(ft.Text(str(fila[6]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16))
                ]
            )
            data_table.rows.append(nueva_fila)
        page.update()

    # Botón de recargar con diseño moderno
    recargar = ft.FilledButton(
        "Recargar",
        on_click=refrescarData,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    # Botón retroceder con icono para mayor intuición
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

    # Contenido con espaciado mejorado
    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([recargar], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([tabla_container], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([boton_retroceder], alignment=ft.MainAxisAlignment.START)
        ],
        spacing=30
    )

    page.add(contenido)

if __name__ == "__main__":
    ft.app(target=main)