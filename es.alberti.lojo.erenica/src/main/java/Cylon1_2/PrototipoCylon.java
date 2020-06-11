package Cylon1_2;

abstract class PrototipoCylon {
    protected String mensaje;

    public void ataque(){
        mensaje = "¡Destruir a todos los humanos!";
    }

    public String getMensaje() {
        return mensaje;
    }
}
