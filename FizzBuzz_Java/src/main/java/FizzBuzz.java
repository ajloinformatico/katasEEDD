public class FizzBuzz {
    /**
     * Comprueba si el numero es divisible de 3
     * calculando si el resto de número/3 es 0 o no
     * @param num int value
     * @return true si es diviesible entre 3, false si no es divisible entre 3
     */

    public boolean fizz(int num){
        if(num % 3 == 0)
            return true;
        return false;
    }

    /**
     * Comprueba si el numero es divisible de 5
     * calculando si el resto de num/5 es 0 o no
     * @param num int value
     * @return true si es diviesible entre 5, false si no es divisible entre 5
     */
    public boolean buzz(int num){
        if(num % 5 == 0)
            return true;
        return false;
    }

    /**
     * Comprueba si el numero es divisible de 5 y de 3
     * calculando si el resto de num/5 y num/3 es 0
     * @param num int value
     * @return true si es diviesible entre 3, false si no es divisible entre 3
     */
    public boolean fizzBuzz(int num){
        if(fizz(num) && buzz(num))
            return true;
        return false;
    }

    /**
     * Comprueba si el numero cumple los requisitos para devolver Fizz, Buzz, o
     * FizzBuzz
     * @param num
     * @return String "Fizz" si fizz() == true, String "buzz" si buzz() == true, String FizzBuzz
     * si fizzBuzz == True
     */
    public String comprobarRango(int num){
        if(fizzBuzz(num))
            return "fizz buzz!";
        else if(buzz(num))
            return "buzz";
        else if(fizz(num))
            return "fizz";
        else
            return "None";
    }

    /**
     * Comprueba si es un numero
     * @param num
     * @return
     */
    public boolean es_numero(String num){
        try {
            Integer.parseInt(num);
            return true;
        } catch (NumberFormatException nfe){
            return false;
        }

    }



}
