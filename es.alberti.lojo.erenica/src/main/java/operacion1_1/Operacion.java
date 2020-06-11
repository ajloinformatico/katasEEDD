package operacion1_1;

abstract class Operacion {
    protected double resultado;
    abstract void ejecuta(double variable1, double variable2);

    public double getResultado() {
        return resultado;
    }
}
