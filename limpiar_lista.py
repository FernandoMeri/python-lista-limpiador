try:
    contactos_unicos = set()
    with open('contactos.txt', 'r') as file_entrada:
        for linea in file_entrada:
            linea_limpia = linea.strip()
            if linea_limpia:
                contactos_unicos.add(linea_limpia)
    with open('contactos_limpios.txt', 'w') as file_salida:
        for contacto in contactos_unicos:
            file_salida.write(contacto + '\n')
    print("La lista se ha limpiado y guardado en 'contactos_limpios.txt'.")
except FileNotFoundError:
    print("Error: El archivo 'contactos.txt' no se encontró")