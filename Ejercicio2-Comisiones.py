# ********************************
# Ejercicio 2: Comisión Vendedores
# ********************************

def obtener_porcentaje_comision(tipo_vendedor):
    if tipo_vendedor == 1:
        return 0.20
    elif tipo_vendedor == 2:
        return 0.15
    elif tipo_vendedor == 3:
        return 0.25
    else:
        return 0


def main():
    total_ventas = 0
    total_comisiones = 0

    while True:
        cedula = int(input("\nIngrese la cédula del vendedor (-1 para terminar): "))
        if cedula == -1:
            break

        nombre = input("Ingrese el nombre del vendedor: ")

        print("\nTipo de vendedor:")
        print("1. Puerta a puerta")
        print("2. Telemercadeo")
        print("3. Ejecutivo de ventas")
        tipo = int(input("Seleccione una opción: "))

        ventas_mes = float(input("Ingrese el valor de ventas del mes: "))

        porcentaje = obtener_porcentaje_comision(tipo)
        comision = ventas_mes * porcentaje

        total_ventas += ventas_mes
        total_comisiones += comision

        print(f"Comisión para {nombre}: ${comision:,.0f}")

    print("\n--- TOTALES DEL MES ---")
    print(f"Total ventas del mes: ${total_ventas:,.0f}")
    print(f"Total a pagar por comisiones: ${total_comisiones:,.0f}")


main()
