import java.util.*;
public class ATM {
    public static void main(String [] args){
        System.out.println("Hello! welcome to Bank of Varada");
        Scanner scn = new Scanner(System.in);

        int pin =1234;

        int addmoney=0;

        int withdrawmoney=0;

        String statement;

        int balance =25000;


        System.out.println("Enter your password :");
        int password = scn.nextInt();
        

        if(password==pin){

            System.out.println("1.addmoney 2.withdrawmoney 3.balance 4.statement ");

            int operation =scn.nextInt();

            switch(operation){
                case 1:
                System.out.println("enter the amout to be added =");
                int amt =scn.nextInt();
                int added = balance +amt;
                System.out.println("The amount is successfully added,now your balance is "+added);
                break;
                case 2:
                System.out.println("enter the amout to be withdrawen =");
                int sub = scn.nextInt();
                if(sub>balance){
                    System.out.println("insufficient balance!");
                
                }
                else{
                    int value = balance-sub;
                    System.out.println("now your balance is: "+value);

                }
                break;
                case 3:
                System.out.println("your balance is :"+balance);
                break;
                case 4:
                System.out.println("your statement :"+balance);
                break;
                default:
                System.out.println("enter value below 5");
                break;

            }
        }
        else{
            System.out.println("register your details into our bank for further processing");
            System.out.println("Thankyou :)");
        }



        
    }    
}
