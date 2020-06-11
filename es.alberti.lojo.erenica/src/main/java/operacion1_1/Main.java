package operacion1_1;

public class Main {
    public static void main (String[] args){
        int n1 = 12;
        int n2 = 23;

        //División
        System.out.println("Implementación División " + n1 + " y " + n2);
        Dividir division = new Dividir();
        division.ejecuta(n1, n2);
        System.out.println( division.getResultado());

        //Multiplicación
        System.out.println("Implementación Multiplicación " + n1 + " y " + n2);
        Multiplicar multiplicacion = new Multiplicar();
        multiplicacion.ejecuta(n1, n2);
        System.out.println(multiplicacion.getResultado());

        //Resta
        System.out.println("Implementación de la resta " + n1 + " y " + n2);
        Restar resta = new Restar();
        resta.ejecuta(n1, n2);
        System.out.println(resta.getResultado());

        //Division
        System.out.println("Implementación de la suma " + n1 + " y " + n2);
        Sumar suma = new Sumar();
        suma.ejecuta(n1, n2);
        System.out.println(suma.getResultado());





    }
}
