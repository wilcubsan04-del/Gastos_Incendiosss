def calcular_gasto(n, costo_inicial, factor):
    if n == 0:
        return costo_inicial

    gasto_anterior = calcular_gasto(n - 1, costo_inicial, factor)
    return gasto_anterior * factor + costo_inicial


costo = 100000
factor = 1.5

consecuencias = [
    "Fallas en sistemas de detección temprana",
    "Insuficiente capacitación de la comunidad",
    "Deficiencia en la formación técnica"
]

print("GASTOS GENERADOS POR EL CONTROL DE INCENDIOS FORESTALES")
print("-" * 55)

for i, consecuencia in enumerate(consecuencias, 1):
    gasto = calcular_gasto(i, costo, factor)

    print(f"Nivel {i}: {consecuencia}")
    print(f"Gasto estimado: ${gasto:,.2f}")
    print()