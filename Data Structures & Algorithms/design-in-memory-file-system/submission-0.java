class Node {
    TreeMap<String, Node> children;
    boolean isFile;
    StringBuilder content;

    Node() {
        children = new TreeMap<>();
        isFile = false;
        content = new StringBuilder();
    }
}

class FileSystem {

    private Node root = new Node();

    public FileSystem() {
        
    }
    
    public List<String> ls(String path) {
        List<String> parts = parsePath(path);
        Node node = parts.isEmpty() ? root : traverseOrCreate(root, parts, false);
        if(node == null){
            return new ArrayList<>();
        }
        if (node.isFile){
            return Arrays.asList(parts.get(parts.size() - 1));
        }

        List<String> result = new ArrayList<>(node.children.keySet());
        Collections.sort(result);
        return result;
    }
    
    public void mkdir(String path) {
        List<String> parts = parsePath(path);
        traverseOrCreate(root, parts, true);
    }
    
    public void addContentToFile(String filePath, String content) {
        List<String> parts = parsePath(filePath);
        if (parts.isEmpty()) return;
        Node node = traverseOrCreate(root, parts, true);
        node.isFile = true;
        node.content.append(content);
    }
    
    public String readContentFromFile(String filePath) {
        List<String> parts = parsePath(filePath);
        if (parts.isEmpty()) return "";
        Node node = traverseOrCreate(root, parts, false);
        if (node == null || !node.isFile) return "";
        return node.content.toString();
    }

    private List<String> parsePath(String path){
        List<String> parts = new ArrayList<>();
        for (String part : path.split("/")){
            if (!part.isEmpty()){
                parts.add(part);
            }
        }

        return parts;
    }

    private Node traverseOrCreate(Node root, List<String> parts, boolean create){
        Node node = root;
        for (String part : parts){
            if(!node.children.containsKey(part)){
                if(!create) return null;
                node.children.put(part, new Node());
            }

            node = node.children.get(part);
        }

        return node;
    }

}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * List<String> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * String param_4 = obj.readContentFromFile(filePath);
 */
