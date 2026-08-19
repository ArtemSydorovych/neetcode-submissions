class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0, current = 0;
        int left = 0;

        var set = new HashSet<Character>();

        for (int right = 0; right < s.length(); right++){
            char c = s.charAt(right);
            
            while (set.contains(c)){
                set.remove(s.charAt(left));
                left++;
            }

            set.add(c);
            res = Math.max(res, right - left + 1);
        }


        return res;
    }
}
