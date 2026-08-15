class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        var hash = new HashMap<String, List<String>>();

        for (var s : strs){
            int[] leters = new int[26];
            for (Character c : s.toCharArray()){
                leters[c - 'a'] += 1;
            }

            var str = Arrays.toString(leters);
            hash.putIfAbsent(str, new ArrayList<>());
            hash.get(str).add(s);
        }

        return new ArrayList<>(hash.values());
    }
}
