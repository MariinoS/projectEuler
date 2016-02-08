// Project Euler: Problem 1 Source Code. By MariinoS. 8th Feb 2016. - Java

// task:   If we list all the natural numbers below 10 that are multiples of 3 or 5,
//         we get 3, 5, 6 and 9. The sum of these multiples is 23.
//         Find the sum of all the multiples of 3 or 5 below 1000.
//
// My Solution:

class problem1{
    public static void main (String[] args){
        int sum = 0;

        for (int i = 1; i < 1000; i++){
            if (i % 3 == 0 || i % 5 == 0)
                sum += i;
        }
        System.out.println(sum);
    }
}

// The script finishes in 0.888s.
// The answer is 233168
