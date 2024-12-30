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
    
    def mostrar_caja(self):
        print(f'Caja actual: {self.caja}')
    
    def mostrar_opciones(self):
        print("Seleccione una moneda:")
        for i, moneda in enumerate(self.caja, start=1):
            print(f'{i}. {moneda}')
    
    def obtener_moneda_por_numero(self, numero):
        lista_monedas = list(self.caja.keys())
        if 1 <= numero <= len(lista_monedas):
            return lista_monedas[numero - 1]
        else:
            return None

def operaciones(opcion, caja_inicial):
    if opcion == "venta":
        caja_inicial.mostrar_opciones()
        seleccion = int(input("Seleccione la moneda que fue vendida (por número): "))
        moneda_entregada = caja_inicial.obtener_moneda_por_numero(seleccion)
        if not moneda_entregada:
            print("Opción no válida.")
            return
        
        cantidad_entregada = int(input(f"Cantidad entregada de {moneda_entregada}: "))
        caja_inicial.mostrar_opciones()
        seleccion = int(input("Seleccione la moneda que fue recibida (por número): "))
        moneda_recibida = caja_inicial.obtener_moneda_por_numero(seleccion)
        if not moneda_recibida:
            print("Opción no válida.")
            return
        
        tipo_de_cambio = float(input("Indique el tipo de cambio: "))
        caja_final = caja_inicial.operacion_venta(moneda_entregada, cantidad_entregada, moneda_recibida, tipo_de_cambio)
        caja_inicial.cambio_caja_venta(caja_final)
        caja_inicial.mostrar_caja()

    elif opcion == "compra":
        caja_inicial.mostrar_opciones()
        seleccion = int(input("Seleccione la moneda que se compró (por número): "))
        moneda_recibida = caja_inicial.obtener_moneda_por_numero(seleccion)
        if not moneda_recibida:
            print("Opción no válida.")
            return
        
        cantidad_comprada = int(input(f"Cantidad comprada de {moneda_recibida}: "))
        caja_inicial.mostrar_opciones()
        seleccion = int(input("Seleccione la moneda entregada (por número): "))
        moneda_entregada = caja_inicial.obtener_moneda_por_numero(seleccion)
        if not moneda_entregada:
            print("Opción no válida.")
            return
        
        tipo_de_cambio = float(input("Indique el tipo de cambio: "))
        caja_final = caja_inicial.operacion_compra(moneda_recibida, cantidad_comprada, moneda_entregada, tipo_de_cambio)
        caja_inicial.cambio_caja_compra(caja_final)
        caja_inicial.mostrar_caja()

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Compra")
    print("2. Venta")
    print("3. Salir")

def main():
    caja_inicial = CajaInicial({"dolar": 10000, "euros": 10000, "pesos argentinos": 10000})
    
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la opción que desea realizar: "))
        
        if opcion == 1:
            operaciones("compra", caja_inicial)
        elif opcion == 2:
            operaciones("venta", caja_inicial)
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

main()



