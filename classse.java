import java.util.*;
public class classse {
    public static void main(String [] args){
       Scanner obj1 = new Scanner(System.in);
            int a=obj1.nextInt();
            int b=obj1.nextInt();
            adding add=new adding();
            int result= add.Per(a,b);
            System.out.print('\n'+result);
    }
}
 class adding{
    
    public int Per(int a1,int b1){
        System.out.println("hello");
        int r=a1+b1;
        return r;
        
    }
    
}