public class Solution {
    private Stack<Character> stack;
    private Queue<Character> queue;
    
    public Solution() {
        this.stack = new Stack<>();
        this.queue = new LinkedList<>();
    }
    
    public void pushCharacter(char ch) {
        stack.push(ch);
    }
    
    public void enqueueCharacter(char ch) {
        queue.add(ch);
    }
    
    public char popCharacter() {
        return stack.pop();
    }
    
    public char dequeueCharacter() {
        return queue.poll();
    }