import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

class FizzBuzzTest {

    @org.junit.jupiter.api.BeforeEach
    void setUp() {
        FizzBuzz f = new FizzBuzz();
    }

    @org.junit.jupiter.api.AfterEach
    void tearDown() {
    }

    /**
     * Comprueba si el numero es divisible de 3
     * calculando si el resto de número/3 es 0 o no
     */
    @org.junit.jupiter.api.Test
    void fizz() {
        FizzBuzz f = new FizzBuzz();
        assertEquals(f.fizz(1),false);
        assertEquals(f.fizz(3),true);
        assertEquals(f.fizz(21),true);
    }

    /**
     * Comprueba si el numero es divisible de 5
     * calculando si el resto de num/5 es 0 o no
     */
    @org.junit.jupiter.api.Test
    void buzz() {
        FizzBuzz f = new FizzBuzz();
        assertEquals(f.buzz(20),true);
        assertEquals(f.buzz(21),false);
        assertEquals(f.buzz(49),false);
        assertEquals(f.buzz(65),true);
    }

    /**
     * Comprueba si el numero es divisible de 5 y de 3
     * calculando si el resto de num/5 y num/3 es 0
     */
    @org.junit.jupiter.api.Test
    void fizzBuzz() {
        FizzBuzz f = new FizzBuzz();
        assertEquals(f.fizzBuzz(42),false);
        assertEquals(f.fizzBuzz(20),false);
        assertEquals(f.fizzBuzz(15),true);
        assertEquals(f.fizzBuzz(90),true);
        assertEquals(f.fizzBuzz(89),false);
    }

    /**
     * Comprueba si el numero cumple los requisitos para devolver Fizz, Buzz, o
     * FizzBuzz
     */
    @org.junit.jupiter.api.Test
    void comprobarRango() {
        FizzBuzz f = new FizzBuzz();
        assertEquals(f.fizzBuzz(42),"fizz");
        assertEquals(f.fizzBuzz(20),"buzz");
        assertEquals(f.fizzBuzz(15),"fizz buzz!");
        assertEquals(f.fizzBuzz(90),"fizz buzz!");
        assertEquals(f.fizzBuzz(89),"None");
    }

    /**
     * Comprueba si es un numero
     */
    @org.junit.jupiter.api.Test
    void es_numero() {
        FizzBuzz f = new FizzBuzz();
        assertEquals(f.es_numero("wewe"),false);
        assertEquals(f.es_numero("2"),true);
    }
}