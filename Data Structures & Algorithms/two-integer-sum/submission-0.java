class Solution {
    public int[] twoSum(int[] nums, int target) {
         var map = new HashMap<Integer, Integer>();

         for(int i = 0; i < nums.length; i++){
            var index = map.getOrDefault(target - nums[i], -1);
            if (index >= 0){
                return new int[]  {index, i};
            }
            map.put(nums[i], i);
         }

         return null;
    }
}
