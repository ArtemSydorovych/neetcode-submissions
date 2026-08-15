class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }
        
        Integer left = 0;
        Integer right = nums.length;
        
        while (right > left){
            if (nums[left] == val){
                nums[left] = nums[--right];
            }
            else{
                left += 1;
            }
        }

        return right;
    }
}