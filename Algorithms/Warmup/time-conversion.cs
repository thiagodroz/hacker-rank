using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
class Solution {

    static string timeConversion(string s) {
        String ampm = s.Substring(s.Length - 2, 2);
        s = s.Remove(s.Length - 2, 2);
        
        int hour = Int32.Parse(s.Substring(0, 2));
        String start = "";
        s = s.Remove(0, 2);
        
        if (ampm == "AM") {
            if (hour == 12) {
              hour = 0;
            }
        } else if (ampm == "PM") {
            hour = hour == 12 ? 12 : hour + 12;
        }
        start = hour.ToString("00");
          
        return String.Concat(start, s);
    }

    static void Main(String[] args) {
        string s = Console.ReadLine();
        string result = timeConversion(s);
        Console.WriteLine(result);
    }
}