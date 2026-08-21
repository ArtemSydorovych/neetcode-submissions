class Solution {
    private static final int[][] dirs = {{0,1}, {1,0}, {-1,0}, {0, -1}};

    public int numIslands(char[][] grid) {
        int count = 0;
        for (int row = 0; row < grid.length; row++){
            for (int column = 0; column < grid[0].length; column++){
                if (grid[row][column] == '1'){
                    dfs(row,column, grid);
                    count++;
                }
            }
        }            

        return count;
    }

    private void dfs(int r, int c, char[][] grid){
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1'){
            return;
        }
        
        grid[r][c] = '2';

        for(int[] d : dirs){
            int nr = r + d[0], nc = c + d[1];
            dfs(nr, nc, grid);
        }
    }
}
