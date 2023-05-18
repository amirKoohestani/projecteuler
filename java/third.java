import java.util.ArrayList;

public class third {
    public static void main(String[] args) {
        long number = 600851475143L;
        ArrayList<Integer> largePrime = new ArrayList<Integer>();
        largePrime.add(2);
        boolean prime = true;

        for(int i = 3; i < (number/2); i++)
            if(number % i == 0){
                for(int j : largePrime){
                    if(i % j == 0){
                        prime = false;
                        break;
                    }
                    if(prime)
                        largePrime.add(i);
                }
            }
        
        System.out.println(largePrime.get(largePrime.size()-1));
    }
}
