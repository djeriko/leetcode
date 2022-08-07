import 'package:test/test.dart';

import 'solution.dart';

void main() {
  Solution solution = Solution();
  test('calculate', () {
    const data = [1, 2, 3, 4];
    const m = 2;
    const r = 2;
    const expected = [
      [1, 2],
      [3, 4]
    ];

    expect(solution.constuct2DArray(data, m, r), expected);
  });
}
