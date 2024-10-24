class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        rows,cols = len(matrix),len(matrix[0])

        zero_row,zero_col = set(),set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
                    zero_row.add(row)
                    zero_col.add(col)
        
        for row in range(rows) :
            for col in range(cols):
                if zero_row in row or zero_col in col:
                    matrix[row][col]=0
