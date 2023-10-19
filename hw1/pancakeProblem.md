题目解释：
你需要处理一个烤饼问题。在这个问题中，每块烤饼的一面都被烤焦了。你的任务是对它们进行翻转，使得烤饼从小到大排列，并且每块烤饼的烤焦面都朝下。

每块烤饼都有一个与其大小相对应的编号（1 到 4），以及一个表示它是否被烤焦的字符（"w"或"b"）。The letter “w” refers to the unburnt (white) side being up, and “b” shows that the burnt side is up.

你的目标是通过翻转操作使得烤饼达到"1w2w3w4w"这个状态。

题目提供了两种搜索算法：广度优先搜索（BFS）和 A\*搜索。你需要根据用户的输入来选择使用哪种算法。

Input:
1b2b3w4b-a # “a” indicates A\*

Output:
1b2b|3w4b g:0, h:0
2w|1w3w4b g:2, h:2
2b1w3w4b| g:3, h:2
4w|3b1b2w g:7, h:4
4b3b1b2w| g:8, h:4
2b1w|3w4w g:12, h:2
1b|2w3w4w g:14, h:0
1w2w3w4w g:15, h:0
