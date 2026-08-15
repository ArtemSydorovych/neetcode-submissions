class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (var n : nums){
            set.add(n);
        }

        return set.size() != nums.length;
    }
}