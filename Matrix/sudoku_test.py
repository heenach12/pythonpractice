class Solution:
    def isValid(self, board):
        # import pdb; pdb.set_trace()
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    print("box_index is",num, box_index)
                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    print("row", rows)
                    print("*********************")
                    print("columns", columns)
                    print("*********************")
                    print("boxes", boxes)
                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return 0
        print("complete rows", rows)
        print("complete colu", columns)
        print("complete box", boxes)

        return 1


t = int(input())
for i in range(t):
    # arr = input().split()
    mat = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    # mat = [[0]*9 for x in range(9)]
    # for i in range(81):
    #     mat[i//9][i%9] = int(arr[i])
    ob = Solution()
    print(ob.isValid(mat))


