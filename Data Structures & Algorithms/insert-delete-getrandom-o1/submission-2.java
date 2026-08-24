class RandomizedSet {
    private final Map<Integer, Integer> map = new HashMap<>();
    private final List<Integer> list = new ArrayList<>();
    private final Random rand = new Random();
    
    public RandomizedSet() {}
    
    public boolean insert(int val) {
        if (map.get(val) != null){
            return false;
        }
            
        map.put(val, list.size());
        list.add(val);

        return true;
        
    }
    
    public boolean remove(int val) {

        if(map.get(val) == null){
            return false;
        }

        int index = map.get(val);

        swapWithLast(index);
        list.remove(list.size() - 1);
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        return list.get(rand.nextInt(list.size()));
    }

    private void swapWithLast(int index){
        if (index == list.size() - 1){
            return;
        }

        int last = list.size() - 1;
        int lastVal = list.get(last);
        int indexVal = list.get(index);

        list.set(index, lastVal);
        list.set(last, indexVal);
        map.put(lastVal, index);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */