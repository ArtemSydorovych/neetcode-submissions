class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int min = 1;
        int max = piles[0];

        for (int pile : piles){
            max = Math.max(pile, max);
        }

        int curMin = max;
        while (min <= max) {
            int k = (min + max) / 2;


            int totalTime = 0;
            for(int pile : piles){
                totalTime += (pile + k - 1)/k;
            }

            if (totalTime <= h){
                curMin = k;
                max = k - 1;
            }else{
                min = k + 1;
            }

        }


        return curMin;
    }
}
