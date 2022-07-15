import 'dart:math' as math;

int maxAreaOfIsland(List<List<int>> grid) {
  final rows = grid.length;
  final cols = grid[0].length;
  final seen = <String>{};
  int maxIsland = 0;

  int dfs(int r, int c) {
    if (r < 0 ||
        r == rows ||
        c < 0 ||
        c == cols ||
        seen.contains('r${r}c$c') ||
        grid[r][c] == 0) {
      return 0;
    }
    seen.add('r${r}c$c');

    return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1);
  }

  for (var i = 0; i < rows; i++) {
    for (var j = 0; j < cols; j++) {
      maxIsland = math.max(maxIsland, dfs(i, j));
    }
  }

  return maxIsland;
}
