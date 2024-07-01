import os

# Lista para almacenar los datos de los vehículos
vehiculos = []

# Función para registrar un vehículo
def registrar_vehiculo():
    marca = input("Ingrese la marca del vehículo: ")
    ano = int(input("Ingrese el año de fabricación: "))
    kilometraje = int(input("Ingrese el kilometraje: "))
    costo_reparacion = float(input("Ingrese el costo de reparación estimado (en pesos): "))
    
    impuesto_servicio = costo_reparacion * 0.08
    costo_total = costo_reparacion + impuesto_servicio
    
    vehiculo = {
        "marca": marca,
        "ano": ano,
        "kilometraje": kilometraje,
        "costo_reparacion": costo_reparacion,
        "impuesto_servicio": impuesto_servicio,
        "costo_total": costo_total
    }
    
    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.\n")

# Función para listar todos los vehículos registrados
def listar_vehiculos():
    if not vehiculos:
        print("No hay vehículos registrados.\n")
        return
    
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Vehículo {i}:")
        print(f"  Marca: {vehiculo['marca']}")
        print(f"  Año de fabricación: {vehiculo['ano']}")
        print(f"  Kilometraje: {vehiculo['kilometraje']}")
        print(f"  Costo de reparación estimado: {vehiculo['costo_reparacion']:.2f}")
        print(f"  Impuesto de servicio: {vehiculo['impuesto_servicio']:.2f}")
        print(f"  Costo total a pagar: {vehiculo['costo_total']:.2f}\n")

# Función para imprimir orden de reparación
def imprimir_orden_reparacion():
    marcas_validas = ["Toyota", "Ford", "Chevrolet"]
    
    print("Seleccione una marca para filtrar:")
    for i, marca in enumerate(marcas_validas, 1):
        print(f"{i}. {marca}")
    
    try:
        opcion = int(input("Ingrese el número de la marca: "))
        if opcion < 1 or opcion > len(marcas_validas):
            print("Opción no válida.\n")
            return
        
        marca_seleccionada = marcas_validas[opcion - 1]
        vehiculos_filtrados = [v for v in vehiculos if v["marca"] == marca_seleccionada]
        
        if not vehiculos_filtrados:
            print(f"No hay vehículos registrados de la marca {marca_seleccionada}.\n")
            return
        
        with open(f"orden_reparacion_{marca_seleccionada}.txt", "w", encoding='utf-8', newline='') as archivo:
            for vehiculo in vehiculos_filtrados:
                archivo.write(f"Marca: {vehiculo['marca']}\n")
                archivo.write(f"Año de fabricación: {vehiculo['ano']}\n")
                archivo.write(f"Kilometraje: {vehiculo['kilometraje']}\n")
                archivo.write(f"Costo de reparación estimado: {vehiculo['costo_reparacion']:.2f}\n")
                archivo.write(f"Impuesto de servicio: {vehiculo['impuesto_servicio']:.2f}\n")
                archivo.write(f"Costo total a pagar: {vehiculo['costo_total']:.2f}\n")
                archivo.write("\n")
        
        print(f"Orden de reparación para la marca {marca_seleccionada} generada exitosamente.\n")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.\n")

# Función principal para mostrar el menú y ejecutar las opciones
def menu_principal():
    while True:
        print("\n" + "="*40)
        print("           MENÚ PRINCIPAL")
        print("="*40)
        print("1. Registrar Vehículo")
        print("2. Listar Todos los Vehículos Registrados")
        print("3. Imprimir Orden de Reparación")
        print("4. Salir")
        print("="*40)

        try:
            opcion = int(input("Ingrese el número de la opción deseada: "))
            print("="*40)

            if opcion == 1:
                registrar_vehiculo()
            elif opcion == 2:
                listar_vehiculos()
            elif opcion == 3:
                imprimir_orden_reparacion()
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.\n")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.\n")

# Función para iniciar la aplicación
def iniciar_aplicacion():
    menu_principal()

# Llamada a la función para iniciar la aplicación
iniciar_aplicacion()