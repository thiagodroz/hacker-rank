    public Difference(int[] elements) {
        this.elements = elements;
    }

    public void computeDifference() {
        int diff = 0;
        
        for (int i = 0; i < elements.length - 1; i++) {
            for (int j = i + 1; j < elements.length; j++) {
                diff = elements[i] - elements[j];
                diff = diff < 0 ? diff * -1 : diff;
                
                if (diff > maximumDifference) {
                    maximumDifference = diff;
                }
            }
        }
    }