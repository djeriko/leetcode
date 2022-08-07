class Solution {
  List<List<int>> constuct2DArray(List<int> data, int cols, int rows) {
    List<List<int>> result = [];

    if (data.length != cols * rows) {
      return result;
    }

    for (int i = 0; i < rows * cols; i + rows) {
      result.add(data.sublist(i, i + rows));
    }

    return result;
  }
}
