//  Project Euler: Problem 4 Source Code. By MariinoS. 21st Feb 2016. - Java

//  Task:   A palindromic number reads the same both ways.
//          The largest palindrome made from the product of
//          two 2-digit numbers is 9009 = 91 × 99.
//          Find the largest palindrome made from the product of two 3-digit numbers.
//
//  My Solution:

import java.util.*;

public class problem4 {
    public static int largestPalindrome(int x){
        int largest = 1;
        // StringBuilder reverse = new StringBuilder(x);
        for (int a = (int)Math.pow(10, (x - 1)); a < (int)Math.pow(10, x); a++ )
            for (int b = (int)Math.pow(10, (x - 1)); b < (int)Math.pow(10, x); b++){
                String original = String.valueOf(a * b);
                String reverse = new StringBuilder(original).reverse().toString();
                if (reverse.equals(original) && (a * b) > largest)
                    largest = a * b;
            }
        return largest;
    }

    public static void main(String[] args) {
        System.out.println(largestPalindrome(3));
    }
}

//  In deze functie wordt iedere berekening 2x uitgevoerd, dit is tijdverlies.
//  Bijvoorbeeld,
//      als x = 3:
//      a en b varieren van 100 tot 999
//      Het product wordt telkens berekend en vergeleken.
//      Maar, 105 * 100 = 100 * 105
//      Het is dus overbodig deze berekiningen allebei uit te voeren.
//      Hoe kan dit vermeden worden?
