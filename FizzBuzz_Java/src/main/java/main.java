public class main {
    public static void main(String args[]) {

        FizzBuzz f = new FizzBuzz();

        for(int num = 1; num<= 100; num++){
            if(f.comprobarRango(num) != "None"){
                System.out.println(f.comprobarRango(num));
            }else{
                System.out.println(num);
            }
        }
    }
}
