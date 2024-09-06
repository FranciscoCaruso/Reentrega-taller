def palabra_mas_larga(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()  # divide el contenido en palabras
            if palabras:  # verifica si hay palabras en el archivo
                palabra_larga = max(palabras, key=len)
                return palabra_larga
            else:
                return "El archivo está vacío."
    except FileNotFoundError:
        return "El archivo no se encontró."

# especifica el nombre del archivo
nombre_archivo = 'texto.txt'
resultado = palabra_mas_larga(nombre_archivo)

print(f"La palabra más larga en el archivo '{nombre_archivo}' es: {resultado}")