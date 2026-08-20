class TimeMap {
    Map<String, List<Entry>> map = new HashMap<>();


    public TimeMap() {}
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(new Entry(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        var entries = map.get(key);

        if(entries == null){
            return "";
        }

        return binarySearch(entries, timestamp);
    }


    private String binarySearch(List<Entry> entries, int timestamp){
        int left = 0, right = entries.size() - 1;
        String result = "";

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (entries.get(mid).timestamp <= timestamp) {
                result = entries.get(mid).value;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    private class Entry{
        public int timestamp;
        public String value;
        
        public Entry(String value, int timestamp){
            this.timestamp = timestamp;
            this.value = value;
        }
    }
}
