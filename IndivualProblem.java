class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();

        // Iterate through the array
        for(int num: nums) {
            
            // Flag to determine if the value has been placed in an existing row
            boolean existInRow= false;

            // Iterate through each row of the matrix
            for(List<Integer> row: ans) {

                // If the number doesn't exist in the current row, add it and set the flag
                if(!row.contains(num)){
                    row.add(num);
                    existInRow = true;
                    break; // Stop checking other rows because the value has been placed
                }
            }

            // If the number couldn't be placed in an existing row, create a new row and add it
            if(!existInRow) {
                List<Integer> newRow = new ArrayList<>();
                newRow.add(num);
                ans.add(newRow);
            }
        }

        return ans;
    }
}