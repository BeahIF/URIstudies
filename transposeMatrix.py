#primeira tentativa
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
#         i = 0
#         j = 0
#         matrix2=matrix
#         print(len(matrix))
#         print(matrix[0][1])
#         while(i<len(matrix)):
#             j=0
#             print(i)
#             while(j<len(matrix[0])):
#                 print(j)
#                 print(matrix[j][i])
#                 matrix2[j][i] = matrix[i][j]
#                 print(matrix2[i][j])
#                 j=j+1
            
#             i=i+1
#         print(matrix2)
#         return matrix2
#forma correta
# 0
# 0
# 1
# 1
# 1
# 2
# 2
# 2
# 3
# 3
# 1
# 0
# 4
# 4
# 1
# 5
# 5
# 2
# 6
# 6
# 2
# 0
# 7
# 7
# 1
# 8
# 8
# 2
# 9
# 9
        result =[[ 0 for i in range(len(matrix)) ] for j in range(len(matrix[0])) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
        return result