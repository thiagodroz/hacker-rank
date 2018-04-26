using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static int[] solve(int[] grades){
        for (int i = 0; i < grades.Length; i++) {
            if (grades[i] >= 38) {
                int nextRounded = ((grades[i] / 5) + 1) * 5;
                if (nextRounded - grades[i] < 3) {
                    grades[i] = nextRounded;
                }
            }
        }
        return grades;
    }

    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        int[] grades = new int[n];
        for(int grades_i = 0; grades_i < n; grades_i++){
           grades[grades_i] = Convert.ToInt32(Console.ReadLine());   
        }
        int[] result = solve(grades);
        Console.WriteLine(String.Join("\n", result));
    }
}
