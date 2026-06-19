# Ejercicio 6.7 - Validación de campos
# Clase EquipoMaratonProgramacion con manejo de excepciones

class EquipoLlenoException(Exception):
    """Excepción lanzada cuando el equipo ya está completo."""
    def __init__(self):
        super().__init__("El equipo ya está completo. No se pueden añadir más programadores.")


class CampoNumericoException(Exception):
    """Excepción lanzada cuando un campo de texto contiene caracteres numéricos."""
    def __init__(self, campo):
        super().__init__(f"El campo '{campo}' no puede contener caracteres numéricos.")


class CampoDemasiadoLargoException(Exception):
    """Excepción lanzada cuando un campo supera los 20 caracteres."""
    def __init__(self, campo):
        super().__init__(f"El campo '{campo}' no puede tener 20 caracteres o más.")


class Programador:
    """Representa a un programador con nombre y apellidos."""

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class EquipoMaratonProgramacion:
    """
    Representa un equipo de programadores para una maratón de programación.

    Atributos:
        nombre_equipo (str): Nombre del equipo.
        universidad (str): Universidad que representa el equipo.
        lenguaje (str): Lenguaje de programación a utilizar.
        tamanio (int): Tamaño máximo del equipo (mínimo 2, máximo 3).
        programadores (list): Lista de programadores del equipo.
    """

    def __init__(self, nombre_equipo, universidad, lenguaje, tamanio):
        if tamanio < 2 or tamanio > 3:
            raise ValueError("El tamaño del equipo debe ser mínimo 2 y máximo 3.")
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamanio = tamanio
        self.programadores = []

    def equipo_completo(self):
        """Determina si el equipo está completo."""
        return len(self.programadores) >= self.tamanio

    def agregar_programador(self, programador):
        """
        Añade un programador al equipo.
        Lanza EquipoLlenoException si el equipo ya está lleno.
        """
        if self.equipo_completo():
            raise EquipoLlenoException()
        self.programadores.append(programador)
        print(f"Programador '{programador}' añadido correctamente.")

    def validar_nombre_apellido(self, valor, campo):
        """
        Valida que un nombre o apellido sea solo texto y tenga menos de 20 caracteres.
        Lanza CampoNumericoException si contiene dígitos.
        Lanza CampoDemasiadoLargoException si tiene 20 o más caracteres.
        """
        if len(valor) >= 20:
            raise CampoDemasiadoLargoException(campo)
        for caracter in valor:
            if caracter.isdigit():
                raise CampoNumericoException(campo)

    def __str__(self):
        info = (
            f"Equipo: {self.nombre_equipo}\n"
            f"Universidad: {self.universidad}\n"
            f"Lenguaje: {self.lenguaje}\n"
            f"Tamaño máximo: {self.tamanio}\n"
            f"Programadores ({len(self.programadores)}/{self.tamanio}):\n"
        )
        for p in self.programadores:
            info += f"  - {p}\n"
        return info


def main():
    print("=== Registro de Equipo para Maratón de Programación ===\n")

    nombre_equipo = input("Nombre del equipo: ")
    universidad = input("Universidad: ")
    lenguaje = input("Lenguaje de programación: ")

    while True:
        try:
            tamanio = int(input("Tamaño del equipo (2 o 3): "))
            equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje, tamanio)
            break
        except ValueError as e:
            print(f"Error: {e}\n")

    print(f"\nIngrese los datos de los {tamanio} programadores:\n")

    while not equipo.equipo_completo():
        print(f"--- Programador {len(equipo.programadores) + 1} ---")

        # Validar nombre
        while True:
            try:
                nombre = input("Nombre: ")
                equipo.validar_nombre_apellido(nombre, "nombre")
                break
            except (CampoNumericoException, CampoDemasiadoLargoException) as e:
                print(f"Error: {e}")

        # Validar apellidos
        while True:
            try:
                apellidos = input("Apellidos: ")
                equipo.validar_nombre_apellido(apellidos, "apellidos")
                break
            except (CampoNumericoException, CampoDemasiadoLargoException) as e:
                print(f"Error: {e}")

        try:
            programador = Programador(nombre, apellidos)
            equipo.agregar_programador(programador)
        except EquipoLlenoException as e:
            print(f"Error: {e}")
            break

        print()

    print("\n=== Información del Equipo Registrado ===")
    print(equipo)


if __name__ == "__main__":
    main()
