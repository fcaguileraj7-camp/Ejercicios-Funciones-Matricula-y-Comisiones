# **********************************
# Ejercicio 1: Liquidación Matrícula
# **********************************

def obtener_valor_matricula(programa):
    if programa == 1:
        return 800000
    elif programa == 2:
        return 1000000
    elif programa == 3:
        return 1200000
    else:
        return 0


def calcular_descuento(valor_matricula, tipo_beca):
    if tipo_beca == 1:
        return valor_matricula * 0.50
    elif tipo_beca == 2:
        return valor_matricula * 0.40
    elif tipo_beca == 3:
        return 0
    else:
        return 0


def main():
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")

    print("\nPrograma académico:")
    print("1. Técnico en Sistemas")
    print("2. Técnico en Desarrollo de Videojuegos")
    print("3. Técnico en Animación Digital")
    programa = int(input("Seleccione una opción: "))

    print("\nTipo de beca:")
    print("1. Beca por rendimiento académico (50%)")
    print("2. Beca cultural/deportes (40%)")
    print("3. Sin beca")
    beca = int(input("Seleccione una opción: "))

    valor_matricula = obtener_valor_matricula(programa)
    descuento = calcular_descuento(valor_matricula, beca)
    valor_final = valor_matricula - descuento

    print("\n--- RESULTADO ---")
    print(f"Estudiante: {nombre}")
    print(f"Valor a pagar por matrícula: ${valor_final:,.0f}")


main()
