package Cylon1_2;

abstract class PrototipoCylon {
    protected String modelo;


    public PrototipoCylon( String modelo){
        this.modelo = modelo;
    }


    public String funcionAtaque(){
        return "Destruir a todos los humanos!!";
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String NewMo){
        this.modelo = NewMo;
    }
}
