import flet as ft
import sqlite3

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Casa de Cambio"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text(
        "Bienvenido",
        size=70,
        color=ft.Colors.BLACK,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    data_table = ft.DataTable(
        bgcolor=ft.Colors.BLUE_GREY_100,
        border=ft.border.all(2, ft.Colors.BLUE_GREY_300),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, ft.Colors.BLUE_GREY_300),
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("FECHA", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("TIPO DE TRANSACCION", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("MONEDA ORIGEN", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("CANTIDAD ORIGEN", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("MONEDA DESTINO", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("CANTIDAD DESTINO", color=ft.Colors.WHITE)),
            ft.DataColumn(ft.Text("TIPO DE CAMBIO", color=ft.Colors.WHITE))
        ],
        rows=[],
        heading_row_color=ft.Colors.BLUE_GREY_700,
        data_row_color=ft.Colors.BLUE_GREY_200
    )

    def refrescarData(e):
        conexion = sqlite3.connect("base-casa-de-cambio.db")
        cursor = conexion.cursor()

        # Obtener todos los registros de la tabla transacciones
        cursor.execute("SELECT * FROM transacciones")
        filas = cursor.fetchall()
        conexion.close()

        data_table.rows.clear()

        # Agregar los datos a la tabla
        for fila in filas:
            nueva_fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(fila[0]), color=ft.Colors.WHITE)),  # ID
                    ft.DataCell(ft.Text(fila[1], color=ft.Colors.WHITE)),  # Fecha
                    ft.DataCell(ft.Text(fila[2], color=ft.Colors.WHITE)),  # Tipo de transacción
                    ft.DataCell(ft.Text(fila[3], color=ft.Colors.WHITE)),  # Moneda origen
                    ft.DataCell(ft.Text(str(fila[4]), color=ft.Colors.WHITE)),  # Cantidad origen
                    ft.DataCell(ft.Text(fila[5], color=ft.Colors.WHITE)),  # Moneda destino
                    ft.DataCell(ft.Text(str(fila[6]), color=ft.Colors.WHITE)),  # Cantidad destino
                    ft.DataCell(ft.Text(str(fila[7]), color=ft.Colors.WHITE))  # Tipo de cambio
                ]
            )
            data_table.rows.append(nueva_fila)
        
        page.update()
    def ingreso_dinero(e):
        return
    def egreso_dinero(e):
        return
    recargar = ft.FilledButton(
        "Recargar",
        on_click=refrescarData,
        width=200,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )
    ingreso = ft.FilledButton(
        "Ingresar de dinero",
        on_click=ingreso_dinero,
        width=300,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )    
    egreso = ft.FilledButton(
        "Egreso de dinero",
        on_click=egreso_dinero,
        width=300,
        height=60,
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=30))
    )  
    texto_fila = ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER)
    boton_fila = ft.Row([recargar,ingreso,egreso], alignment=ft.MainAxisAlignment.CENTER)

    contenido = ft.Column(
        controls=[texto_fila, boton_fila, data_table],
        spacing=20
    )

    page.add(contenido)

if __name__ == "__main__":
    ft.app(target=main)
