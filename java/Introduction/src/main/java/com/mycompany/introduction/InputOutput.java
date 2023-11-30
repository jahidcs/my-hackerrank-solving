package com.mycompany.introduction;
import java.util.Scanner;

public class InputOutput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int a, b, c;
        
        a = scanner.nextInt();
        b = scanner.nextInt();
        c = scanner.nextInt();
        
        scanner.close();
        
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}
