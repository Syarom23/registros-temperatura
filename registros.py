registros = [
    {"sensor": "S01", "temperatura": 24.5, "ubicacion": "Zona A"},
    {"sensor": "S02", "temperatura": 38.2, "ubicacion": "Zona B"},
    {"sensor": "S03", "temperatura": -80.0, "ubicacion": "Zona A"},
    {"sensor": "S04", "temperatura": 31.0, "ubicacion": "Zona B"},
    {"sensor": "S05", "temperatura": "Vacío", "ubicacion": "Zona A"}
]

validos_temperaturas = []
validos_estados = []

rechazados_temperaturas = []
rechazados_motivos = []

for r in registros:
    temp = r["temperatura"]
    es_numero = (type(temp) == int) or (type(temp) == float)
    
    if es_numero:
        if temp >= -50 and temp <= 100:
            validos_temperaturas.append(temp)
            if temp >= 35:
                validos_estados.append("ALTA")
            else:
                validos_estados.append("NORMAL")
        else:
            rechazados_temperaturas.append(temp)
            rechazados_motivos.append("Fuera de rango")
    else:
        rechazados_temperaturas.append(temp)
        rechazados_motivos.append("No es un número")

print("Válidas:", validos_temperaturas)
print("Estados:", validos_estados)
print("Rechazadas:", rechazados_temperaturas)
print("Motivos:", rechazados_motivos)




# ## Fase 2
# # C
# if (temperatura >= -50.0 && temperatura <= 100.0):
# //se abre el archivo utilizando la función fopen(), se utiliza un bucle while para recorrer línea por línea
# # SQL
# SELECT temperatura, ubicacion 
# FROM mediciones 
# WHERE temperatura >= -50 AND temperatura <= 100;
