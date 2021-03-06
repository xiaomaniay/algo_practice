class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        if not board:
            return False
        board = [list(x) for x in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        tempt = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i + 1, j, word[1:]) \
              or self.dfs(board, i, j - 1, word[1:]) or self.dfs(board, i, j + 1, word[1:])
        board[i][j] = tempt
        return res


if __name__ == "__main__":
    board = ["ABCE", "SFES", "ADEE"]
    word = "ABCESEEEFS"
    print(Solution().exist(board, word))
