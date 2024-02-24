import java.util.Scanner;
public class sumofevenno {
   
    public static void main(String [] args){

        System.out.println("hello this is a code for sum of even numbers");
        Scanner value= new Scanner(System.in);
        
         int num = value.nextInt();
         //int sum=0;

if(num%2==0){
    
    System.out.println("It is an even no");

//using for loop
for(int i= 0; i <=10; i++){
    num +=2;
System.out.println(num);}
}

else{
    System.out.print("IT is a odd no");
}

    }

}


    

