class Solution {
    private static final int[][] DIRS = {{1,0}, {0,1}, {-1,0}, {0,-1}}; 


    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color){
            return image;
        }

        dfs(image, sr, sc, image[sr][sc], color);

        return image;
    }

    private void dfs(int[][] image, int r, int c, int orig, int color){
        if(r < 0 || r >= image.length || c < 0 || c >= image[0].length || image[r][c] != orig){
            return;
        }

        image[r][c] = color;
        for(int[] d : DIRS){
            dfs(image, r + d[0], c + d[1], orig, color);
        }
    }
}