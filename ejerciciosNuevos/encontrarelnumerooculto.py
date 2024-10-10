#encontrar el numero oculto
import java.util.Random;
import java.util.Scanner;

public class AdivinaElNumero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int numeroOculto = random.nextInt(100) + 1; // Genera un número entre 1 y 100
        int intentos = 10;
        boolean adivinado = false;

        System.out.println("¡Bienvenido al juego de Adivina el Número!");
        System.out.println("He seleccionado un número entre 1 y 100.");
        System.out.println("Tienes " + intentos + " intentos para adivinarlo.");

        while (intentos > 0 && !adivinado) {
            System.out.print("Introduce tu suposición: ");
            int suposicion = scanner.nextInt();
            intentos--;

            if (suposicion == numeroOculto) {
                adivinado = true;
                System.out.println("¡Felicidades! Has adivinado el número.");
            } else if (suposicion < numeroOculto) {
                System.out.println("Demasiado bajo. Te quedan " + intentos + " intentos
