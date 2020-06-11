package Cylon1_2;

abstract class PrototipoCylon {
    protected String mensaje;
    protected String ataque = "Destruir a todos los humanos";
    protected String modelo;

    public String ataque(){
        return ataque;
    }

    public String getMensaje() {
        return mensaje;
    }

    public String getModelo() {
        return modelo;
    }

    public void setMensaje(String NewMe){
        this.mensaje = NewMe;
    }

    public void setModelo(String NewMo){
        this.modelo = NewMo;
    }


}
