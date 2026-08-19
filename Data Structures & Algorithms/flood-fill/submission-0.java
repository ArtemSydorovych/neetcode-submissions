class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color){
            return image;
        }

        int m = image.length;
        int n = image[0].length;

        dfs(image, sr, sc, image[sr][sc], color, m, n);

        return image;
    }

    private void dfs(int[][] image, int r, int c, int orig, int color, int m, int n){
        if(r < 0 || r >= m || c < 0 || c >= n || image[r][c] != orig){
            return;
        }

        image[r][c] = color;
        dfs(image, r + 1, c, orig, color, m, n);
        dfs(image, r - 1, c, orig, color, m, n);
        dfs(image, r, c + 1, orig, color, m, n);
        dfs(image, r, c - 1, orig, color, m, n);
    }
}