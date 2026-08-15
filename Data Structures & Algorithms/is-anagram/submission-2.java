class Solution {
    public boolean isAnagram(String s, String t) {
        var mapS = new HashMap<Character, Integer>();
        var mapT = new HashMap<Character, Integer>();

        if (s.length() != t.length()){
            return false;
        }

        for (int i  = 0; i < s.length(); i++){
            mapS.merge(s.charAt(i), 1, Integer::sum);
            mapT.merge(t.charAt(i), 1, Integer::sum);
        }


        return mapS.equals(mapT);
    }
}
