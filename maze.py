import queue

def solution(map):
    row = len(map)
    column = len(map[0])

    def grid(i, j, map):
        Q = queue.Queue()
        Q.put((i, j))
        move = [[0 for i in range(column)] for j in range(row)]
        move[i][j] = 1
        while Q.empty() != True:
            (a, b) = Q.get()
            for inc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newi = a + inc[0]
                newj = b + inc[1]

                if 0 <= newi < row and 0 <= newj < column and move[newi][newj] == 0:
                    move[newi][newj] = move[a][b] + 1
                    if map[newi][newj] == 1:
                        continue
                    else:
                        Q.put((newi, newj))
        return move
    gridb = grid(0, 0, map)
    return gridb[row-1][column-1]
