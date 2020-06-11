package Cylon1_2;

import sun.swing.MenuItemCheckIconFactory;

public class Hibrido extends PrototipoCylon implements Humanos {
    boolean enchufa = false;

    public Hibrido(){
        this.modelo = "humano";
        this.enchufa = enchufa;

    }

    @Override
    public boolean desconecta_conecta(boolean yes_no) {
        if(yes_no == true)
            return true;
        return false;
    }
}
