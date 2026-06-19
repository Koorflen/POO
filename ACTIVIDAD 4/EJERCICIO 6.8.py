# Ejercicio 6.8 - Lectura de archivos
# Clase LeerArchivo que lee un archivo de texto usando flujo de bytes

class LeerArchivo:
    """
    Lee un archivo de texto y muestra su contenido por pantalla.
    """

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer(self):
        """
        Abre el archivo en modo binario (flujo de bytes), lo decodifica
        y muestra su contenido línea a línea por pantalla.
        Lanza IOError si ocurre un problema de entrada/salida.
        """
        try:
            # Abrimos en modo binario ('rb')
            with open(self.ruta_archivo, 'rb') as flujo_bytes:
                # Decodificamos los bytes a texto Unicode
                contenido_bytes = flujo_bytes.read()
                contenido_texto = contenido_bytes.decode('utf-8')

                # Leemos línea a línea
                lineas = contenido_texto.splitlines()
                print(f"=== Contenido de '{self.ruta_archivo}' ===\n")
                for linea in lineas:
                    print(linea)

                print(f"\n=== Fin del archivo ({len(lineas)} líneas leídas) ===")

        except FileNotFoundError:
            raise IOError(f"No se encontró el archivo '{self.ruta_archivo}'.")
        except PermissionError:
            raise IOError(f"Sin permisos para leer el archivo '{self.ruta_archivo}'.")
        except UnicodeDecodeError:
            raise IOError(f"Error al decodificar el archivo '{self.ruta_archivo}'. "
                          "Verifique que sea un archivo de texto UTF-8.")


def main():
    ruta = "prueba.txt"
    lector = LeerArchivo(ruta)
    try:
        lector.leer()
    except IOError as e:
        print(f"Error de E/S: {e}")


if __name__ == "__main__":
    main()
