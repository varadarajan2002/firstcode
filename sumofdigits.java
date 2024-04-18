import java.util.*;

public class Sumofdigits{
	public static void main(String args[]){
		int num,digit,sum =0;
		Scanner n = new Scanner(System.in);
                System.out.print("Enter the value or the number =");
		num = n.nextInt();
		
	while(num>0){
		digit = num%10;
		sum = sum+digit;
		num=num/10;
}
System.out.print("The sum of the digits is = " +sum);
}
}
