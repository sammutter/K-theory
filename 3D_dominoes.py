#! /usr/bin/python

import math
import numpy as np
import time

# q = 5
# label = [0,1,2]
# unpt_tiles = [[12,1,-12,-1],[12,2,-12,-2],[12,5,-12,-5],[12,6,-12,-6],[12,9,-12,-9],[12,10,-12,-10],
# [4,1,-4,-1],[4,2,-4,-2],[4,5,-4,-5],[4,6,-4,-6],[4,9,-4,-9],[4,10,-4,-10],
# [8,1,-8,-1],[8,2,-8,-2],[8,5,-8,-5],[8,6,-8,-6],[8,9,-8,-9],[8,10,-8,-10],
# [1,2,-1,-2],[1,6,-1,-6],[1,10,-1,-10],
# [5,2,-5,-2],[5,6,-5,-6],[5,10,-5,-10],
# [9,2,-9,-2],[9,6,-9,-6],[9,10,-9,-10]]

# 5, 0,1,3
# q = 5
# label = [0,1,3]
# old_tiles = [[0, 1, 16, 21], [0, 3, 4, 19], [0, 5, 8, 9], [0, 7, 0, 11], [0, 9, 8, 5], [0, 13, 20, 13], [0, 15, 20, 23], [0, 17, 4, 17], [0, 19, 4, 3], [0, 21, 16, 1], [0, 23, 20, 15], [1, 3, 17, 3], [1, 4, 5, 20], [1, 7, 13, 19], [1, 11, 9, 11], [1, 15, 1, 23], [1, 20, 5, 4], [3, 5, 19, 5], [3, 9, 15, 21], [3, 16, 23, 16], [3, 20, 7, 20], [4, 7, 8, 23], [4, 21, 8, 21], [4, 23, 8, 7], [5, 7, 21, 7], [5, 11, 17, 23], [7, 9, 23, 9]]

# 5, 1,2,3
# q = 5
# label = [1,2,3]
# old_tiles = [[1, 2, 17, 22], [1, 3, 17, 3], [1, 6, 9, 10], [1, 7, 13, 19], [1, 10, 9, 6], [1, 11, 9, 11], [1, 14, 21, 14], [1, 15, 1, 23], [1, 18, 5, 18], [1, 22, 17, 2], [2, 3, 18, 23], [2, 5, 6, 21], [2, 7, 10, 11], [2, 11, 10, 7], [2, 15, 22, 15], [2, 19, 6, 19], [2, 21, 6, 5], [2, 23, 18, 3], [3, 5, 19, 5], [3, 6, 7, 22], [3, 9, 15, 21], [3, 22, 7, 6], [5, 7, 21, 7], [5, 11, 17, 23], [5, 22, 9, 22], [6, 23, 10, 23], [7, 9, 23, 9]]

# 26 tiles example
# unpt_tiles = [[12,1,4,5],[12,5,4,-1],[12,9,-4,1],[12,-9,12,-5],[12,-1,-4,9],[4,9,4,-5],
#              [12,2,-4,-6],[12,6,-12,10],[12,10,-4,-14],[12,14,12,-2],[12,-14,4,6],[12,-10,4,2],[4,10,4,-6],[4,14,-4,2],
#              [2,1,10,-9],[2,5,14,-5],[2,9,-14,5],[2,-9,14,9],[2,-5,6,1],[2,-1,14,-1],[6,5,-10,-9],[6,9,14,1],[6,-9,10,9],[6,-5,10,5],[6,-1,10,-1],[10,1,14,5]]

# 27 tiles example
#unpt_tiles = [[12,1,-4,-9],[12,5,8,9],[12,9,8,5],[12,-1,-8,-1],[12,-5,4,-5],[12,-9,-4,1],[4,1,-8,5],[4,5,-8,1],[4,-9,8,-9],[12,3,-4,3],[12,7,-12,-7],[12,11,8,11],[12,-3,12,-11],[4,3,4,-7],[4,7,-8,7],[4,11,-4,-11],[8,3,-8,-3],[8,7,8,-11],[1,3,-5,-11],[1,7,9,11],[1,11,9,7],[1,-3,-9,-3],[1,-7,5,-7],[1,-11,-5,3],[5,3,-9,7],[5,7,-9,3],[5,-11,9,-11]]

# q = 5
# label = [0,1,3]


# 2.01 x F13
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34],[8,38,-8,-38],[4,38,-4,-38],[8,42,-8,-42],[4,42,-4,-42],[8,46,-8,-46],[4,46,-4,-46],[8,50,-8,-50],[4,50,-4,-50], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34],[1,38,-1,-38],[5,38,-5,-38],[1,42,-1,-42],[5,42,-5,-42],[1,46,-1,-46],[5,46,-5,-46],[1,50,-1,-50],[5,50,-5,-50]]
# 2.01 x F9
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34]]
# 2.01 x F8
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30]]
# 2.01 x F7
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26]]
# 2.01 x F6
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22]]
# 2.01 x F5
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18]]
# 2.01 x F4
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14]]
# 2.01 x F3
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10]]
# 2.01 x F2
# unpt_tiles = [[8,1,8,-1],[8,5,8,-5],[4,1,4,-1],[4,5,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6]]

# 2.23 x F13
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34],[8,38,-8,-38],[4,38,-4,-38],[8,42,-8,-42],[4,42,-4,-42],[8,46,-8,-46],[4,46,-4,-46],[8,50,-8,-50],[4,50,-4,-50], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34],[1,38,-1,-38],[5,38,-5,-38],[1,42,-1,-42],[5,42,-5,-42],[1,46,-1,-46],[5,46,-5,-46],[1,50,-1,-50],[5,50,-5,-50]]
# 2.23 x F9
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34]]
# 2.23 x F8
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30]]
# 2.23 x F7
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26]]
# 2.23 x F6
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22]]
# 2.23 x F5
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18]]
# 2.23 x F4
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14]]
# 2.23 x F3
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10]]
# 2.23 x F2
# unpt_tiles = [[8,1,8,-1],[8,5,-8,-5],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6]]

# 2.11 x F13
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34],[8,38,-8,-38],[4,38,-4,-38],[8,42,-8,-42],[4,42,-4,-42],[8,46,-8,-46],[4,46,-4,-46],[8,50,-8,-50],[4,50,-4,-50], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34],[1,38,-1,-38],[5,38,-5,-38],[1,42,-1,-42],[5,42,-5,-42],[1,46,-1,-46],[5,46,-5,-46],[1,50,-1,-50],[5,50,-5,-50]]
# 2.11 x F9
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34]]
# 2.11 x F8
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30]]
# 2.11 x F7
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26]]
# 2.11 x F6
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22]]
# 2.11 x F5
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18]]
# 2.11 x F4
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14]]
# 2.11 x F3
# unpt_tiles = [[8,1,8,-1],[8,5,-8,5],[4,1,4,5],[4,-1,4,-5], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10]]

# 2.47 x F13
# unpt_tiles = [[8,1,-8,5],[8,5,-8,-1],[4,1,-4,5],[4,5,-4,-1], [8,2,-8,-2],[4,2,-4,-2],[8,6,-8,-6],[4,6,-4,-6],[8,10,-8,-10],[4,10,-4,-10],[8,14,-8,-14],[4,14,-4,-14],[8,18,-8,-18],[4,18,-4,-18],[8,22,-8,-22],[4,22,-4,-22],[8,26,-8,-26],[4,26,-4,-26],[8,30,-8,-30],[4,30,-4,-30],[8,34,-8,-34],[4,34,-4,-34],[8,38,-8,-38],[4,38,-4,-38],[8,42,-8,-42],[4,42,-4,-42],[8,46,-8,-46],[4,46,-4,-46],[8,50,-8,-50],[4,50,-4,-50], [1,2,-1,-2],[5,2,-5,-2],[1,6,-1,-6],[5,6,-5,-6],[1,10,-1,-10],[5,10,-5,-10],[1,14,-1,-14],[5,14,-5,-14],[1,18,-1,-18],[5,18,-5,-18],[1,22,-1,-22],[5,22,-5,-22],[1,26,-1,-26],[5,26,-5,-26],[1,30,-1,-30],[5,30,-5,-30],[1,34,-1,-34],[5,34,-5,-34],[1,38,-1,-38],[5,38,-5,-38],[1,42,-1,-42],[5,42,-5,-42],[1,46,-1,-46],[5,46,-5,-46],[1,50,-1,-50],[5,50,-5,-50]]

# q = 5
# label = [1,2,3]

# 2.01 x 2.01 x 2.24
# unpt_tiles = [[8, 1, 8, -1], [8, 5, 4, 5], [8, -5, 4, -5], [4, 1, 4, -1], [8, 2, 8, -2], [8, 6, 8, -6], [4, 2, 4, -2], [4, 6, 4, -6], [1, 2, 1, -2], [1, 6, 1, -6], [5, 2, 5, -2], [5, 6, 5, -6]]
    
# unpt_tiles = [[1, 2, 1, -2], [1, 6, 1, -6], [5, 2, 5, -2], [5, 6, 5, -6], [3, 1, 3, -1], [3, 5, 3, -5], [7, 1, 7, -1], [7, 5, 7, -5], [2, 3, 2, -3], [2, 7, 2, -7], [6, 3, 6, -3], [6, 7, 6, -7]]
#----------------------------------------------------

# q = 7             
# label = [2,4,5]
# old_tiles = [[2, 4, 32, 46], [2, 5, 44, 17], [2, 10, 26, 34], [2, 11, 8, 23], [2, 16, 20, 22], [2, 17, 44, 5], [2, 22, 20, 16], [2, 23, 8, 11], [2, 28, 38, 28], [2, 29, 38, 35], [2, 35, 38, 29], [2, 40, 14, 40], [2, 41, 14, 47], [2, 46, 32, 4], [2, 47, 14, 41], [4, 5, 16, 23], [4, 8, 10, 38], [4, 11, 40, 41], [4, 17, 22, 17], [4, 20, 28, 44], [4, 23, 16, 5], [4, 29, 4, 35], [4, 38, 10, 8], [4, 41, 40, 11], [4, 47, 34, 47], [5, 8, 47, 20], [5, 10, 5, 40], [5, 20, 47, 8], [5, 22, 47, 22], [5, 32, 41, 38], [5, 34, 35, 46], [5, 38, 41, 32], [5, 46, 35, 34], [8, 16, 32, 40], [8, 34, 44, 34], [8, 35, 44, 41], [8, 41, 44, 35], [8, 46, 20, 46], [10, 14, 16, 44], [10, 17, 46, 47], [10, 35, 10, 41], [10, 44, 16, 14], [10, 47, 46, 17], [11, 16, 11, 46], [11, 38, 47, 44], [11, 44, 47, 38], [14, 22, 38, 46], [16, 41, 16, 47]]

# q=7
# label = [0,1,5]
# old_tiles = [[0, 1, 42, 1], [0, 5, 18, 5], [0, 7, 6, 7], [0, 11, 42, 23], [0, 13, 0, 43], [0, 17, 6, 29], [0, 19, 36, 25], [0, 23, 42, 11], [0, 25, 36, 19], [0, 29, 6, 17], [0, 31, 12, 37], [0, 35, 30, 35], [0, 37, 12, 31], [0, 41, 0, 47], [1, 5, 31, 11], [1, 6, 19, 6], [1, 11, 31, 5], [1, 17, 25, 41], [1, 18, 7, 30], [1, 23, 19, 29], [1, 29, 19, 23], [1, 30, 7, 18], [1, 35, 1, 47], [1, 36, 31, 36], [5, 6, 47, 6], [5, 7, 41, 7], [5, 12, 11, 12], [5, 13, 29, 37], [5, 19, 17, 19], [5, 36, 17, 42], [5, 42, 17, 36], [6, 13, 12, 13], [6, 23, 12, 35], [6, 35, 12, 23], [6, 37, 18, 43], [6, 41, 36, 41], [6, 43, 18, 37], [7, 11, 37, 17], [7, 17, 37, 11], [7, 23, 31, 47], [7, 42, 37, 42], [11, 13, 47, 13], [11, 18, 17, 18], [11, 19, 35, 43], [12, 19, 18, 19], [12, 47, 42, 47], [13, 17, 43, 23], [13, 23, 43, 17]]

#----------------------------------------------------
q=5
label = [1,2,3]
old_tiles = [[1, 2, 17, 22], [1, 3, 17, 3], [1, 6, 9, 10], [1, 7, 13, 19], [1, 10, 9, 6], [1, 11, 9, 11], [1, 14, 21, 14], [1, 15, 1, 23], [1, 18, 5, 18], [1, 22, 17, 2], [2, 3, 18, 23], [2, 5, 6, 21], [2, 7, 10, 11], [2, 11, 10, 7], [2, 15, 22, 15], [2, 19, 6, 19], [2, 21, 6, 5], [2, 23, 18, 3], [3, 5, 19, 5], [3, 6, 7, 22], [3, 9, 15, 21], [3, 22, 7, 6], [5, 7, 21, 7], [5, 11, 17, 23], [5, 22, 9, 22], [6, 23, 10, 23], [7, 9, 23, 9]]

# Products of free Abelian groups
# q = 5
# label = [0,1,2, "3,4,13"]
# unpt_tiles = [[12, 1, -12, -1], [12, 5, -12, -5], [12, 9, -12, -9], [12, 13, -12, -13], [4, 1, -4, -1], [4, 5, -4, -5], [4, 9, -4, -9], [4, 13, -4, -13], [8, 1, -8, -1], [8, 5, -8, -5], [8, 9, -8, -9], [8, 13, -8, -13], [12, 2, -12, -2], [12, 6, -12, -6], [12, 10, -12, -10], [12, 14, -12, -14], [12, 18, -12, -18], [12, 22, -12, -22], [12, 26, -12, -26], [12, 30, -12, -30], [12, 34, -12, -34], [12, 38, -12, -38], [12, 42, -12, -42], [12, 46, -12, -46], [12, 50, -12, -50], [4, 2, -4, -2], [4, 6, -4, -6], [4, 10, -4, -10], [4, 14, -4, -14], [4, 18, -4, -18], [4, 22, -4, -22], [4, 26, -4, -26], [4, 30, -4, -30], [4, 34, -4, -34], [4, 38, -4, -38], [4, 42, -4, -42], [4, 46, -4, -46], [4, 50, -4, -50], [8, 2, -8, -2], [8, 6, -8, -6], [8, 10, -8, -10], [8, 14, -8, -14], [8, 18, -8, -18], [8, 22, -8, -22], [8, 26, -8, -26], [8, 30, -8, -30], [8, 34, -8, -34], [8, 38, -8, -38], [8, 42, -8, -42], [8, 46, -8, -46], [8, 50, -8, -50], [1, 2, -1, -2], [1, 6, -1, -6], [1, 10, -1, -10], [1, 14, -1, -14], [1, 18, -1, -18], [1, 22, -1, -22], [1, 26, -1, -26], [1, 30, -1, -30], [1, 34, -1, -34], [1, 38, -1, -38], [1, 42, -1, -42], [1, 46, -1, -46], [1, 50, -1, -50], [5, 2, -5, -2], [5, 6, -5, -6], [5, 10, -5, -10], [5, 14, -5, -14], [5, 18, -5, -18], [5, 22, -5, -22], [5, 26, -5, -26], [5, 30, -5, -30], [5, 34, -5, -34], [5, 38, -5, -38], [5, 42, -5, -42], [5, 46, -5, -46], [5, 50, -5, -50], [9, 2, -9, -2], [9, 6, -9, -6], [9, 10, -9, -10], [9, 14, -9, -14], [9, 18, -9, -18], [9, 22, -9, -22], [9, 26, -9, -26], [9, 30, -9, -30], [9, 34, -9, -34], [9, 38, -9, -38], [9, 42, -9, -42], [9, 46, -9, -46], [9, 50, -9, -50], [13, 2, -13, -2], [13, 6, -13, -6], [13, 10, -13, -10], [13, 14, -13, -14], [13, 18, -13, -18], [13, 22, -13, -22], [13, 26, -13, -26], [13, 30, -13, -30], [13, 34, -13, -34], [13, 38, -13, -38], [13, 42, -13, -42], [13, 46, -13, -46], [13, 50, -13, -50]]

# unpt_tiles = [
#     [1, 2, -1, -2], [1, 6, -1, -6], [5, 2, -5, -2], [5, 6, -5, -6], [3, 1, -3, -1], 
#     [3, 5, -3, -5], [7, 1, -7, -1], [7, 5, -7, -5], [3, 2, -3, -2], [3, 6, -3, -6], 
#     [7, 2, -7, -2], [7, 6, -7, -6]
# ]

tiles = []
all_tiles = []
k = 3
start_time = time.time()

# Tiles' labels come in two types: if they comprise only positive integers, run this function to convert them to positive and negative integers
def convert_3d(old_list, label):
    z = int((q**2 - 1)/2)
    new_list = []
    for tile in old_list:
        new_tile = [z - y if y > z or y == 0 else y for y in tile]
        new_list.append(new_tile)
    return new_list 

unpt_tiles = convert_3d(old_tiles, label)
print("tiles list:", unpt_tiles)

r = len(unpt_tiles)

# From which sets are the edges of tile T and block C?
def face_type(T):
    return [abs(T[0]) % (q - 1) , abs(T[1]) % (q - 1)]
def block_type(C):
    return [abs(C[0][0]) % (q - 1) , abs(C[0][1]) % (q - 1) , abs(C[1][0]) % (q - 1)]

# Functions which return the symmetries of an unpointed tile T.
def horiz(T):
    return [-T[0],-T[3],-T[2],-T[1]]
def vert(T):
    return [-T[2],-T[1],-T[0],-T[3]]
def rot(T):
    return[T[2],T[3],T[0],T[1]]

for i in range(r):
    tiles = tiles + [unpt_tiles[i]] + [horiz(unpt_tiles[i])] + [vert(unpt_tiles[i])] + [rot(unpt_tiles[i])]

# Contains all tiles twice: once type ab and once type ba.   
for T in tiles:
    all_tiles = all_tiles + [T] + [[T[1],T[2],T[3],T[0]]]

# Run on T from all_tiles to find all cubes based at T.
def cubes_based_at(T):
    cube_list = []
    sides_adj = []
    tiles_same_type = []
    tiles_other_type = []
    # Decide if another tile is adjacent to T
    for U in all_tiles:
        if set(face_type(U)) != set(face_type(T)):
            tiles_other_type.append(U)
            if face_type(U)[1] == face_type(T)[0] and U[3] == -T[0]:
                sides_adj.append(U)
        else:
            tiles_same_type.append(U)
    
    # Build cubes uniquely-defined by two adjacent squares: T and U from sides_adj
    for U in sides_adj:
        cube = [T,U,0,0,0,0]
        for V in tiles_other_type:
            if V[0] == -T[3] and V[3] == -U[0]:
                cube[2] = V
                for W in tiles_same_type:
                    if W[0] == -U[1] and W[1] == -V[2]:
                        cube[3] = W
                for W in tiles_other_type:
                    if W[0] == -V[1] and W[1] == -T[2] and W[3] == -cube[3][2]:
                        cube[4] = W
                    if W[0] == -T[1] and W[1] == -U[2] and W[2] == -cube[3][3]:
                        cube[5] = W

        if 0 in cube:
            print('Error: no valid tile found to complete cube:', cube)
        else:
            cube_list.append(cube)
    return cube_list
    
def cubes_based_from(tileset):
    cubes_list = []
    for T in tileset:
        cubes_list = cubes_list + cubes_based_at(T)
    return cubes_list

# All 3-dim cubes in all orientations.
all_cubes = cubes_based_from(all_tiles)
print("all_cubes done")

# # Functions which return the symmetries of an unpointed cube C.
# def hor0(C):
#     return [hor(C[0]), ver(C[1]), hor(C[5]), hor(C[3]), ver(C[4]), hor(C[2])]
# def ver0(C):
#     return [ver(C[0]), hor(C[4]), hor(C[2]), ver(C[3]), hor(C[1]), hor(C[5])]
# def rot0(C):
#     return [rot(C[0]), rot(C[4]), C[5], rot(C[3]), rot(C[1]), C[2]]
# def inv0(C):
#     return [hor(C[3]), hor(C[1]), ver(C[2]), hor(C[0]), hor(C[4]), ver(C[5])]
# def horinv(C):
#     return [C[3], rot(C[1]), rot(C[5]), C[0], rot(C[4]), rot(C[2])]
# def verinv(C):
#     return [rot(C[3]), C[4], rot(C[2]), rot(C[0]), C[1], rot(C[5])]
# def rotinv(C):
#     return [ver(C[3]), ver(C[4]), ver(C[5]), ver(C[0]), ver(C[1]), ver(C[2])]

# # Set of all cubes symmetric to a given cube.
# def cube_symmetries(C):
#     return [C, hor0(C), ver0(C), rot0(C), inv0(C), horinv(C), verinv(C), rotinv(C)]


# Functions which return the symmetries of a cube C.
def hornorm(C):
    return [horiz(C[0]),vert(C[1]),horiz(C[5]),horiz(C[3]),vert(C[4]),horiz(C[2])]
def vernorm(C):
    return [vert(C[0]),horiz(C[4]),horiz(C[2]),vert(C[3]),horiz(C[1]),horiz(C[5])]
def rotnorm(C):
    return [rot(C[0]),rot(C[4]),C[5],rot(C[3]),rot(C[1]),C[2]]
def inv(C):
    return [horiz(C[3]),horiz(C[1]),vert(C[2]),horiz(C[0]),horiz(C[4]),vert(C[5])]
def horinv(C):
    return [C[3],rot(C[1]),rot(C[5]),C[0],rot(C[4]),rot(C[2])]
def verinv(C):
    return [rot(C[3]),C[4],rot(C[2]),rot(C[0]),C[1],rot(C[5])]
def rotinv(C):
    return [vert(C[3]),vert(C[4]),vert(C[5]),vert(C[0]),vert(C[1]),vert(C[2])]

def cube_symmetries(C):
    return [C,hornorm(C),vernorm(C),rotnorm(C),inv(C),horinv(C),verinv(C),rotinv(C)]

# Kill unwanted duplicate cubes, and then add in precisely one of each symmetry.
def eliminate_dupl(cubeset):
    cube_syms = []
    small_cubeset = []
    for C in cubeset:
        if C in cube_syms:
            continue
        else:
            small_cubeset.append(C)
            cube_syms = cube_syms + cube_symmetries(C)
    return small_cubeset

def tiles_type_x(tileset,x):
    outpt = []
    for T in tileset:
        if face_type(T) == x:
            outpt.append(T)
    return outpt

# This is the list of all pointed cubes (geometric cubes and their 2^k symmetries)
pt_cubes = []
unpt_cubes = []

for C in eliminate_dupl(cubes_based_from(tiles_type_x(all_tiles,[label[0], label[1]]))):
    unpt_cubes.append(C)
    pt_cubes = pt_cubes + cube_symmetries(C)
    
print("elim dupl done")

n = len(pt_cubes)



# -----------------------------------------------------------------

# Adjacency functions for the set pt_cubes.
def f1(A,B):
    if A[1] == horiz(B[4]) and A[0][1] != -B[0][1]:
        adjacency = 1
    else:
        adjacency = 0
    return adjacency
def f2(A,B):
    if A[2] == horiz(B[5]) and A[0][0] != -B[0][0]:
        adjacency = 1
    else:
        adjacency = 0
    return adjacency
def f3(A,B):
    if A[0] == horiz(B[3]) and A[1][0] != -B[1][0]:
        adjacency = 1
    else:
        adjacency = 0
    return adjacency

# Matrices from Evans.

M1 = []
for A in pt_cubes:
    new_row = []
    for B in pt_cubes:
        new_row.append(f1(A,B))
    M1.append(new_row)
M1 = np.array(M1)
M1T = np.transpose(M1)
print("M1 done")

M2 = []
for A in pt_cubes:
    new_row = []
    for B in pt_cubes:
        new_row.append(f2(A,B))
    M2.append(new_row)
M2 = np.array(M2)
M2T = np.transpose(M2)
print("M2 done")

M3 = []
for A in pt_cubes:
    new_row = []
    for B in pt_cubes:
        new_row.append(f3(A,B))
    M3.append(new_row)
M3 = np.array(M3)
M3T = np.transpose(M3)
print("M3 done")

I = np.eye(n,dtype=int)
O = np.zeros((n,n),dtype=int)

d1 = np.block([I-M1T,I-M2T,I-M3T])
d2 = np.block([[M2T-I,M3T-I,O],[I-M1T,O,M3T-I],[O,I-M1T,I-M2T]])
d3 = np.block([[I-M3T],[M2T-I],[I-M1T]])
print("big matrices done")


# Write a string of the relations of the group homomorphism d, where the generators of the image are string y.
def group_rels(d,y):
    rels = ''
    num_rows = len(d)
    num_cols = len(d[0])
    for j in range(num_cols):
        for i in range(num_rows):
            if d[i][j] == 0:
                pass
            else:
                rels = rels + str(d[i][j]) + '*' + y + '[' + str(i+1) + '] + '
        rels = rels[0:len(rels)-3] + ', '
    rels = rels[0:len(rels)-2]
    return rels

# Print code readable by MAGMA.
def print_homs():
    txtfile = "3D_wow_{}_{}.txt".format(q, label)
    f = open(txtfile, "a")

    print('A<[a]> := FreeAbelianGroup(',len(d3[0]),');', file=f)
    print('B<[b]> := FreeAbelianGroup(',len(d2[0]),');', file=f)
    print('C<[c]> := FreeAbelianGroup(',len(d1[0]),');', file=f)
    print('D<[d]> := FreeAbelianGroup(',len(d3[0]),');', file=f)

    print('d1 := hom< C -> D | ',group_rels(d1,'d'),'>;', file=f)
    print('K1 := Kernel(d1);', file=f)
    print('d2 := hom< B -> K1 | ',group_rels(d2,'c'),'>;', file=f)
    print('K2 := Kernel(d2);', file=f)
    print('d3 := hom< A -> K2 | ',group_rels(d3,'b'),'>;', file=f)
    print('K3 := Kernel(d3);', file=f)

    f.close()
    print("done")
    
    
# Uncomment one of these functions
# print_homs()
print(unpt_cubes)
print(len(unpt_cubes))
# print(pt_cubes)
# print(len(pt_cubes))
# print(pt_cubes[0])

end_time = time.time()
total_time = end_time - start_time
print("***************")
print("This took", round(total_time, 3), "seconds.")

# Write the maps as matrices.
# def mat_rep(d,name):
#     num_rows = len(d)
#     num_cols = len(d[0])
#     matr = name + ':= Matrix(IntegerRing(),' + str(num_rows) + ',' + str(num_cols) + ',['
#     for i in range(num_rows):
#         for j in range(num_cols):
#             matr = matr + str(d[i][j]) + ','
#     matr = matr[0:len(matr)-1]
#     matr = matr + ']);'
#     return matr

# print(mat_rep(d1,'d1'))
# print(mat_rep(d2,'d2'))
# print(mat_rep(d3,'d3'))

   
#print(all_tiles) 
#print(len(all_tiles))
#print(len(pt_cubes))
