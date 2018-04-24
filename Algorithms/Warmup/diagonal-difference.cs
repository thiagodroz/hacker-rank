using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {
    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        int[][] a = new int[n][];
        for(int a_i = 0; a_i < n; a_i++){
           string[] a_temp = Console.ReadLine().Split(' ');
           a[a_i] = Array.ConvertAll(a_temp,Int32.Parse);
        }
        
        int diagonal1 = 0;
        int diagonal2 = 0;
        
        for (int i = 0; i < a.Length; i++) {
            diagonal1 += a[i][i];
            diagonal2 += a[i][a.Length - i - 1];
            
        }
        
        Console.WriteLine(diagonal1 > diagonal2 ? diagonal1 - diagonal2 : diagonal2 - diagonal1);
    }
}