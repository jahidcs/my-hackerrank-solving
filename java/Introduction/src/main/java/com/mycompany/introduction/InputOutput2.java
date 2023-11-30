package com.mycompany.introduction;
import java.util.Scanner;

public class InputOutput2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String s;
        double d;
        int i;
        
        i = scanner.nextInt();
        d = scanner.nextDouble();
        scanner.nextLine();
        s = scanner.nextLine();
        
        scanner.close();
        
        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
    
}
