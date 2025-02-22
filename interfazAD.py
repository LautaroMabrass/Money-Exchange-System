import flet as ft
import mysql.connector
import db_config
from datetime import datetime

def cargar_saldos():
    try:
        conn = mysql.connector.connect(**db_config.DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute('SELECT USD, ARS, CLP, EUR FROM caja ORDER BY id DESC LIMIT 1')
        saldos = cursor.fetchone()
        if saldos is None:
            return {'USD': 0, 'ARS': 0, 'CLP': 0, 'EUR': 0}
        return {'USD': saldos[0], 'ARS': saldos[1], 'CLP': saldos[2], 'EUR': saldos[3]}
    except mysql.connector.Error as e:
        print(f"Error al cargar saldos: {e}")
        return {'USD': 0, 'ARS': 0, 'CLP': 0, 'EUR': 0}
    finally:
        cursor.close()
        conn.close()

def main(page: ft.Page):
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

    texto = ft.Text(
        "Bienvenido, ¿qué deseas hacer hoy?",
        size=60,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

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

    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([transacciones, cajas], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ],
        spacing=30
    )

    page.add(contenido)

def caja(page: ft.Page):
    saldos = cargar_saldos()

    texto = ft.Text(
        "Caja Actual",
        size=45,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.GREY_400))
    )

    saldos_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row([ft.Icon(ft.Icons.ATTACH_MONEY), ft.Text(f"Dólares: {saldos['USD']:.2f}", size=20)]),
                ft.Row([ft.Icon(ft.Icons.MONETIZATION_ON), ft.Text(f"Pesos Argentinos: {saldos['ARS']:.2f}", size=20)]),
                ft.Row([ft.Icon(ft.Icons.MONETIZATION_ON), ft.Text(f"Pesos Chilenos: {saldos['CLP']:.2f}", size=20)]),
                ft.Row([ft.Icon(ft.Icons.EURO), ft.Text(f"Euros: {saldos['EUR']:.2f}", size=20)])
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=10,
        shadow=ft.BoxShadow(blur_radius=10, spread_radius=2, color=ft.Colors.GREY_400)
    )

    def refrescarData(e):
        saldos = cargar_saldos()
        saldos_container.content.controls[0].controls[1].value = f"Dólares: {saldos['USD']:.2f}"
        saldos_container.content.controls[1].controls[1].value = f"Pesos Argentinos: {saldos['ARS']:.2f}"
        saldos_container.content.controls[2].controls[1].value = f"Pesos Chilenos: {saldos['CLP']:.2f}"
        saldos_container.content.controls[3].controls[1].value = f"Euros: {saldos['EUR']:.2f}"
        page.update()

    def retroceder(e):
        page.controls.clear()
        main(page)
        page.update()

    def ir_ingresar_dinero(e):
        page.controls.clear()
        ingresar_dinero_view(page)
        page.update()

    def ir_egresar_dinero(e):
        page.controls.clear()
        egresar_dinero_view(page)
        page.update()

    def ir_modificar_todo(e):
        page.controls.clear()
        modificar_caja_view(page)
        page.update()

    ingreso_boton = ft.FilledButton(
        "Ingresar",
        icon=ft.Icons.ADD,
        on_click=ir_ingresar_dinero,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8),
            elevation=5
        )
    )

    egreso_boton = ft.FilledButton(
        "Egresar",
        icon=ft.Icons.REMOVE,
        on_click=ir_egresar_dinero,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8),
            elevation=5
        )
    )

    modificar_todo_boton = ft.FilledButton(
        "Modificar",
        icon=ft.Icons.EDIT,
        on_click=ir_modificar_todo,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8),
            elevation=5
        )
    )

    recargar = ft.FilledButton(
        "Recargar",
        icon=ft.Icons.REFRESH,
        on_click=refrescarData,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8),
            elevation=5
        )
    )

    ver_operaciones_boton = ft.FilledButton(
        "Ver Operaciones",
        icon=ft.Icons.LIST,
        on_click=lambda e: mostrar_operaciones(page),
        width=300,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8),
            elevation=5
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
            shape=ft.RoundedRectangleBorder(radius=8),
            elevation=5
        )
    )

    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([saldos_container], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ingreso_boton, egreso_boton, modificar_todo_boton], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Row([recargar, ver_operaciones_boton], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Row([boton_retroceder], alignment=ft.MainAxisAlignment.START)
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Casa de Cambio - Caja"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(contenido)

def modificar_caja_view(page: ft.Page):
    saldos = cargar_saldos()
    usd = ft.TextField(label="Dólares", width=200, border_color=ft.Colors.INDIGO_700, value=str(saldos['USD']))
    ars = ft.TextField(label="Pesos Argentinos", width=200, border_color=ft.Colors.INDIGO_700, value=str(saldos['ARS']))
    clp = ft.TextField(label="Pesos Chilenos", width=200, border_color=ft.Colors.INDIGO_700, value=str(saldos['CLP']))
    eur = ft.TextField(label="Euros", width=200, border_color=ft.Colors.INDIGO_700, value=str(saldos['EUR']))

    def confirmar_modificacion(e):
        try:
            nuevos_saldos = {
                'USD': float(usd.value),
                'ARS': float(ars.value),
                'CLP': float(clp.value),
                'EUR': float(eur.value)
            }
            if any(val < 0 for val in nuevos_saldos.values()):
                raise ValueError("Los montos no pueden ser negativos")
            conn = mysql.connector.connect(**db_config.DB_CONFIG)
            cursor = conn.cursor()
            # Obtener el id máximo primero
            cursor.execute('SELECT MAX(id) FROM caja')
            max_id = cursor.fetchone()[0]
            if max_id is not None:
                # Actualizar la tabla con el id obtenido
                saldos_anteriores = cargar_saldos()
                cursor.execute('UPDATE caja SET USD = %s, ARS = %s, CLP = %s, EUR = %s WHERE id = %s',
                               (nuevos_saldos['USD'], nuevos_saldos['ARS'], nuevos_saldos['CLP'], nuevos_saldos['EUR'], max_id))
                conn.commit()
                saldos_nuevos = cargar_saldos()
                cursor.execute('''
                    INSERT INTO operaciones_caja (
                        fecha, tipo_operacion, moneda, cantidad,
                        saldo_anterior_USD, saldo_anterior_ARS, saldo_anterior_CLP, saldo_anterior_EUR,
                        saldo_nuevo_USD, saldo_nuevo_ARS, saldo_nuevo_CLP, saldo_nuevo_EUR
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'modificacion',
                    None,
                    None,
                    saldos_anteriores['USD'], saldos_anteriores['ARS'], saldos_anteriores['CLP'], saldos_anteriores['EUR'],
                    saldos_nuevos['USD'], saldos_nuevos['ARS'], saldos_nuevos['CLP'], saldos_nuevos['EUR']
                ))
                conn.commit()
                page.controls.clear()
                caja(page)
                page.update()
            else:
                snack_bar = ft.SnackBar(ft.Text("No hay registros en la tabla caja para modificar"))
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
        except ValueError as ve:
            snack_bar = ft.SnackBar(ft.Text(str(ve)))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        except mysql.connector.Error as e:
            snack_bar = ft.SnackBar(ft.Text(f"Error en la base de datos: {e}"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        finally:
            cursor.close()
            conn.close()

    confirmar_boton = ft.FilledButton(
        "Confirmar",
        on_click=confirmar_modificacion,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    def retroceder(e):
        page.controls.clear()
        caja(page)
        page.update()

    retroceder_boton = ft.FilledButton(
        "Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    contenido = ft.Column(
        controls=[
            ft.Row([ft.Text("Modificar Caja", size=45, color=ft.Colors.GREY_800, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([usd], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ars], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([clp], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([eur], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([confirmar_boton, retroceder_boton], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(contenido)
    page.update()

def ingresar_dinero_view(page: ft.Page):
    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Ingresar Dinero"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text(
        "Ingresar Dinero",
        size=45,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    moneda = ft.Dropdown(
        label="Moneda",
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("ARS"),
            ft.dropdown.Option("CLP"),
            ft.dropdown.Option("EUR"),
        ],
        width=200,
        border_color=ft.Colors.INDIGO_700
    )
    cantidad = ft.TextField(label="Cantidad", width=200, border_color=ft.Colors.INDIGO_700)

    def confirmar_ingreso(e):
        if moneda.value and cantidad.value:
            try:
                monto = float(cantidad.value)
                if monto <= 0:
                    raise ValueError("El monto debe ser positivo")
                conn = mysql.connector.connect(**db_config.DB_CONFIG)
                cursor = conn.cursor()
                # Obtener el id máximo primero
                cursor.execute('SELECT MAX(id) FROM caja')
                max_id = cursor.fetchone()[0]
                if max_id is not None:
                    saldos_anteriores = cargar_saldos()
                    # Actualizar la tabla con el id obtenido
                    cursor.execute(f'UPDATE caja SET {moneda.value} = {moneda.value} + %s WHERE id = %s', (monto, max_id))
                    conn.commit()
                    saldos_nuevos = cargar_saldos()
                    cursor.execute('''
                        INSERT INTO operaciones_caja (
                            fecha, tipo_operacion, moneda, cantidad,
                            saldo_anterior_USD, saldo_anterior_ARS, saldo_anterior_CLP, saldo_anterior_EUR,
                            saldo_nuevo_USD, saldo_nuevo_ARS, saldo_nuevo_CLP, saldo_nuevo_EUR
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'ingreso',
                        moneda.value,
                        monto,
                        saldos_anteriores['USD'], saldos_anteriores['ARS'], saldos_anteriores['CLP'], saldos_anteriores['EUR'],
                        saldos_nuevos['USD'], saldos_nuevos['ARS'], saldos_nuevos['CLP'], saldos_nuevos['EUR']
                    ))
                    conn.commit()
                    page.controls.clear()
                    caja(page)
                    page.update()
                else:
                    snack_bar = ft.SnackBar(ft.Text("No hay registros en la tabla caja para modificar"))
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            except ValueError as ve:
                snack_bar = ft.SnackBar(ft.Text(str(ve)))
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            except mysql.connector.Error as e:
                snack_bar = ft.SnackBar(ft.Text(f"Error en la base de datos: {e}"))
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            finally:
                cursor.close()
                conn.close()

    def retroceder(e):
        page.controls.clear()
        caja(page)
        page.update()

    confirmar_boton = ft.FilledButton(
        "Confirmar",
        on_click=confirmar_ingreso,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    retroceder_boton = ft.FilledButton(
        "Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([moneda], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([cantidad], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([confirmar_boton, retroceder_boton], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(contenido)

def egresar_dinero_view(page: ft.Page):
    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Egresar Dinero"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text(
        "Egresar Dinero",
        size=45,
        color=ft.Colors.GREY_800,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    moneda = ft.Dropdown(
        label="Moneda",
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("ARS"),
            ft.dropdown.Option("CLP"),
            ft.dropdown.Option("EUR"),
        ],
        width=200,
        border_color=ft.Colors.INDIGO_700
    )
    cantidad = ft.TextField(label="Cantidad", width=200, border_color=ft.Colors.INDIGO_700)

    def confirmar_egreso(e):
        if moneda.value and cantidad.value:
            try:
                monto = float(cantidad.value)
                if monto <= 0:
                    raise ValueError("El monto debe ser positivo")
                saldos = cargar_saldos()
                if monto > saldos[moneda.value]:
                    raise ValueError("Fondos insuficientes")
                conn = mysql.connector.connect(**db_config.DB_CONFIG)
                cursor = conn.cursor()
                # Obtener el id máximo primero
                cursor.execute('SELECT MAX(id) FROM caja')
                max_id = cursor.fetchone()[0]
                if max_id is not None:
                    saldos_anteriores = cargar_saldos()
                    # Actualizar la tabla con el id obtenido
                    cursor.execute(f'UPDATE caja SET {moneda.value} = {moneda.value} - %s WHERE id = %s', (monto, max_id))
                    conn.commit()
                    saldos_nuevos = cargar_saldos()
                    cursor.execute('''
                        INSERT INTO operaciones_caja (
                            fecha, tipo_operacion, moneda, cantidad,
                            saldo_anterior_USD, saldo_anterior_ARS, saldo_anterior_CLP, saldo_anterior_EUR,
                            saldo_nuevo_USD, saldo_nuevo_ARS, saldo_nuevo_CLP, saldo_nuevo_EUR
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'egreso',
                        moneda.value,
                        monto,
                        saldos_anteriores['USD'], saldos_anteriores['ARS'], saldos_anteriores['CLP'], saldos_anteriores['EUR'],
                        saldos_nuevos['USD'], saldos_nuevos['ARS'], saldos_nuevos['CLP'], saldos_nuevos['EUR']
                    ))
                    conn.commit()
                    page.controls.clear()
                    caja(page)
                    page.update()
                else:
                    snack_bar = ft.SnackBar(ft.Text("No hay registros en la tabla caja para modificar"))
                    page.overlay.append(snack_bar)
                    snack_bar.open = True
                    page.update()
            except ValueError as ve:
                snack_bar = ft.SnackBar(ft.Text(str(ve)))
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            except mysql.connector.Error as e:
                snack_bar = ft.SnackBar(ft.Text(f"Error en la base de datos: {e}"))
                page.overlay.append(snack_bar)
                snack_bar.open = True
                page.update()
            finally:
                cursor.close()
                conn.close()

    def retroceder(e):
        page.controls.clear()
        caja(page)
        page.update()

    confirmar_boton = ft.FilledButton(
        "Confirmar",
        on_click=confirmar_egreso,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    retroceder_boton = ft.FilledButton(
        "Retroceder",
        icon=ft.Icons.ARROW_BACK,
        on_click=retroceder,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    contenido = ft.Column(
        controls=[
            ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([moneda], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([cantidad], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([confirmar_boton, retroceder_boton], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        ],
        spacing=30,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(contenido)

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
        try:
            conn = mysql.connector.connect(**db_config.DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT fecha, tipo_transaccion, moneda_origen, cantidad_origen, moneda_destino, cantidad_destino, tipo_cambio FROM transacciones")
            filas = cursor.fetchall()
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
        except mysql.connector.Error as e:
            snack_bar = ft.SnackBar(ft.Text(f"Error al cargar transacciones: {e}"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        finally:
            cursor.close()
            conn.close()

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
    refrescarData(None)

def mostrar_operaciones(page: ft.Page):
    page.controls.clear()
    page.bgcolor = ft.Colors.INDIGO_50
    page.title = "Casa de Cambio - Operaciones de Caja"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text(
        "Operaciones de Caja",
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
            ft.DataColumn(ft.Text("TIPO", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("MONEDA", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("CANTIDAD", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO ANTERIOR USD", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO ANTERIOR ARS", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO ANTERIOR CLP", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO ANTERIOR EUR", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO NUEVO USD", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO NUEVO ARS", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO NUEVO CLP", color=ft.Colors.BLACK, size=18)),
            ft.DataColumn(ft.Text("SALDO NUEVO EUR", color=ft.Colors.BLACK, size=18)),
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

    def refrescar_operaciones(e):
        try:
            conn = mysql.connector.connect(**db_config.DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT fecha, tipo_operacion, moneda, cantidad, saldo_anterior_USD, saldo_anterior_ARS, saldo_anterior_CLP, saldo_anterior_EUR, saldo_nuevo_USD, saldo_nuevo_ARS, saldo_nuevo_CLP, saldo_nuevo_EUR FROM operaciones_caja")
            filas = cursor.fetchall()
            data_table.rows.clear()
            for fila in filas:
                nueva_fila = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(fila[0], color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                        ft.DataCell(ft.Text(fila[1], color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                        ft.DataCell(ft.Text(fila[2] if fila[2] else "N/A", color=ft.Colors.BLACK, text_align=ft.TextAlign.LEFT, size=16)),
                        ft.DataCell(ft.Text(str(fila[3]) if fila[3] else "N/A", color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[4]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[5]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[6]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[7]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[8]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[9]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[10]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                        ft.DataCell(ft.Text(str(fila[11]), color=ft.Colors.BLACK, text_align=ft.TextAlign.RIGHT, size=16)),
                    ]
                )
                data_table.rows.append(nueva_fila)
            page.update()
        except mysql.connector.Error as e:
            snack_bar = ft.SnackBar(ft.Text(f"Error al cargar operaciones: {e}"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
        finally:
            cursor.close()
            conn.close()

    recargar = ft.FilledButton(
        "Recargar",
        on_click=refrescar_operaciones,
        width=200,
        height=60,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.INDIGO_700,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=24),
            shape=ft.RoundedRectangleBorder(radius=8)
        )
    )

    def retroceder(e):
        page.controls.clear()
        caja(page)
        page.update()

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
    refrescar_operaciones(None)

if __name__ == "__main__":
    ft.app(target=main)