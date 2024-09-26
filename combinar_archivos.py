def combinar_archivos(archivo1ej3, archivo2ej3):
    try:
        # abre ambos archivos para lectura
        with open(archivo1ej3, 'r', encoding='utf-8') as file1, open(archivo2ej3, 'r', encoding='utf-8') as file2:
           
            lineas1 = file1.readlines()
            lineas2 = file2.readlines()

        # mismo número de líneas
        lineas_combinadas = []
        for l1, l2 in zip(lineas1, lineas2):
            lineas_combinadas.append(l1.strip() + " " + l2.strip())  # elimina espacios

      
        with open(archivo2ej3, 'w', encoding='utf-8') as file2:
            file2.write('\n'.join(lineas_combinadas)) #las une con esspeacios en el medio 
        
        print(f"Archivo combinado correctamente y guardado en '{archivo2ej3}'.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")


archivo1ej3 = 'archivo1ej3.txt'
archivo2ej3 = 'archivo2ej3.txt'
combinar_archivos(archivo1ej3, archivo2ej3)
