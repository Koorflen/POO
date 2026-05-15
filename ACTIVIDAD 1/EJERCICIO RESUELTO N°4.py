class Calculate_ages:
    
    @staticmethod
    def calculate_age_alber(age_juan):
        age_alber = int(2 * age_juan / 3)
        return age_alber

    @staticmethod
    def calculate_age_ana(age_juan):
        age_ana = int(4 * age_juan / 3)
        return age_ana

    @staticmethod
    def calculate_age_mama(age_juan):
        age_mama = int(age_juan + age_alber + age_ana)
        return age_mama

age_juan = -1

while age_juan <= 0:
    
    try:
        Input = input("Ingrese la edad de Juan: ").replace(",", ".")
        Input = float(Input)
        
        if Input != int(Input) and not Input > 0:
            print("Por favor, ingrese un número entero positivo.")

        elif Input != int(Input):
            print("Por favor, ingrese un número entero.")
            
        elif Input <= 0:
            print("La edad debe ser un número positivo. Intente nuevamente.")
            
        else:
            age_juan = int(Input)
            
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

age_alber = Calculate_ages.calculate_age_alber(age_juan)
age_ana = Calculate_ages.calculate_age_ana(age_juan)
age_mama = Calculate_ages.calculate_age_mama(age_juan)

print(f"La edad de Juan es: {age_juan} años\n"
      f"La edad de Alberto es: {age_alber} años\n"
      f"La edad de Ana es: {age_ana} años\n"
      f"La edad de la Mamá es: {age_mama} años")