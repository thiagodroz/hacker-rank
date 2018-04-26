class Student : Person{
    private int[] testScores;  
  
    /*	
    *   Class Constructor
    *   
    *   Parameters: 
    *   firstName - A string denoting the Person's first name.
    *   lastName - A string denoting the Person's last name.
    *   id - An integer denoting the Person's ID number.
    *   scores - An array of integers denoting the Person's test scores.
    */
    public Student(String firstName, String lastName, int id, int[] scores) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.id = id;
        this.testScores = scores;
    }
    
    /*	
    *   Method Name: Calculate
    *   Return: A character denoting the grade.
    */
    public String Calculate() {
        int sum = 0;
        float average = 0;
        
        foreach (int score in this.testScores) {
            sum += score;
        }
        
        average = sum / testScores.Length;
        
        if (average >= 90.0) {
            return "O";
        } else if (average >= 80.0) {
            return "E";
        } else if (average >= 70.0) {
            return "A";
        } else if (average >= 55.0) {
            return "P";
        } else if (average >= 40.0) {
            return "D";
        } else {
            return "T";
        }
    }
}