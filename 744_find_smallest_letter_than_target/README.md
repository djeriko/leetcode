#### ***744.Find Smallest Letter Hreater Than Target***

Level - Easy

Given a character array letter that is sorted in non-decreasing order and a
character target, return the smallest character in the array that is larger than
target.

None that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


***Example 1:***
```
Input: letters = ["c", "f", "j"] , target = "a"
Output: "c"
```

***Example 2:***
```
Input: letters = ["c", "f", "j"], target = "c"
Output: "f"
```

***Example 3:***
```
Input: letters = ["c", "f", "j"], target = "d"
Output: "f"
```

Constratins:
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter.
- letters is sorted in non-decreasing order.
- letters contains at least two different characters.
- target is a lowercase English letter.
