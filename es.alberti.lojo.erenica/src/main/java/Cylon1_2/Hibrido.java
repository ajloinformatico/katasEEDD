package Cylon1_2;

public class Hibrido extends Pellejudo implements Humanos {
    private boolean desc_con;

    public Hibrido(boolean desc_con) {
        this.desc_con = desc_con;
    }

    @Override
    public boolean conectaDes() {
        return this.desc_con;
    }
}
