import java.util.Scanner;

class CalculateAges {

    public static int calculateageAlber(int ageJuan) {
        return (int) (2.0 * ageJuan / 3.0);
    }

    public static int calculateageAna(int ageJuan) {
        return (int) (4.0 * ageJuan / 3.0);
    }

    public static int calculateageMama(int ageJuan) {
        return ageJuan + calculateageAlber(ageJuan) + calculateageAna(ageJuan);
    }
}

public class EJERCICIO_RESUELTO_N4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int ageJuan = -1;

        while (ageJuan <= 0) {
            try {
                System.out.print("Ingrese la edad de Juan: ");
                String input = scanner.nextLine().replace(",", ".");
                double val = Double.parseDouble(input);

                if (val != (int)val && val < 0) {
                    System.out.println("Por favor, ingrese un número entero positivo.");
                } else if (val != (int)val) {
                    System.out.println("Por favor, ingrese un número entero.");
                } else if (val <= 0) {
                    System.out.println("La edad debe ser un número positivo. Intente nuevamente.");
                } else {
                    ageJuan = (int)val;
                }
            } catch (NumberFormatException e) {
                System.out.println("Entrada no válida. Por favor, ingrese un número entero.");
            }
        }

        // Llamamos a los métodos estáticos de nuestra clase de lógica
        int ageAlber = CalculateAges.calculateageAlber(ageJuan);
        int ageAna = CalculateAges.calculateageAna(ageJuan);
        int ageMama = CalculateAges.calculateageMama(ageJuan);
        
        System.out.println("La edad de Juan es: " + ageJuan + " años\n" +
                           "La edad de Alberto es: " + ageAlber + " años\n" +
                           "La edad de Ana es: " + ageAna + " años\n" +
                           "La edad de la Mamá es: " + ageMama + " años");
        
        scanner.close(); // Buena práctica: cerrar el scanner al terminar
    }
}

