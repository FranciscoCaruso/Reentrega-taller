def combinar_archivos(archivo1ej3, archivo2ej3):
    try:
        # Abre ambos archivos para lectura
        with open(archivo1ej3, 'r', encoding='utf-8') as file1, open(archivo2ej3, 'r', encoding='utf-8') as file2:
            # Lee las líneas de ambos archivos
            lineas1 = file1.readlines()
            lineas2 = file2.readlines()

        # Asegura que ambos archivos tengan el mismo número de líneas
        lineas_combinadas = []
        for l1, l2 in zip(lineas1, lineas2):
            lineas_combinadas.append(l1.strip() + " " + l2.strip())  # Concatena y agrega un espacio entre ambas líneas

        # Escribe el resultado en el segundo archivo
        with open(archivo2ej3, 'w', encoding='utf-8') as file2:
            file2.write('\n'.join(lineas_combinadas))
        
        print(f"Archivo combinado correctamente y guardado en '{archivo2ej3}'.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejemplo de uso
archivo1ej3 = 'archivo1ej3.txt'
archivo2ej3 = 'archivo2ej3.txt'
combinar_archivos(archivo1ej3, archivo2ej3)
