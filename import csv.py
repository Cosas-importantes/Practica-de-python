import csv

# Cambia estos valores según tu configuración
nombre_archivo = 'invitados.csv'
nombre_tabla = 'invitados'

# Abrir el archivo CSV y leer los datos
with open(nombre_archivo, 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')
    for fila in lector_csv:
        sentencia_sql = f"INSERT INTO {nombre_tabla} (nombre, asistira, comida, completado, telefono, grupo_familiar, apellido, DNI, habilitado, anotaciones) VALUES "
        sentencia_sql += f"('{fila['nombre']}', '{fila['asistira']}', '{fila['comida']}', '{fila['completado']}', '{fila['telefono']}', '{fila['grupo_familiar']}', '{fila['apellido']}', '{fila['DNI']}', '{fila['habilitado']}', '{fila['anotaciones']}')"
        print(sentencia_sql)
