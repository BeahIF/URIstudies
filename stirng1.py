# def removeAdj(v,n):
#     # Your code goes here
    
#     # print(v)
#     # print(n)
#     # print(len(v))
#     i=0
#     j=1
#     while(i < len(v)-1 and j<len(v)):
#         test=v[i]
#         print(test)
#         print(v[j])
#         if(test == v[j]):
#             print("aqui")
#             del(v[i])
#             del(v[j-1])
#             print("i")
#             print(i)
#             print("j")
#             print(j)
#             auxI= i
#         print(len(v))
#         if(j>len(v)):
#             i=i+1
#             j=1
#             print("no if")
#         else:
#             print("no else")
#             j=j+1

           
#     print(v)
#     print(len(v))
# # removeAdj(["ab", "aa", "aa", "bcd", "ab"]
# SOLUCAO:
# Python3 program to remove consecutive
# same words

# Function to find the size of
# manipulated sequence
def removeConsecutiveSame(v):

	n = len(v)

	# Start traversing the sequence
	i = 0
	while(i < n - 1):
		
		# Compare the current string with
		# next one Erase both if equal
		if ((i + 1) < len(v)) and (v[i] == v[i + 1]):
		
			# Erase function delete the element and
			# also shifts other element that's why
			# i is not updated
			v = v[:i]
			v = v[:i]
			# Update i, as to check from previous
			# element again
			if (i > 0):
				i -= 1

			# Reduce sequence size
			n = n - 2
		
		# Increment i, if not equal
		else:
			i += 1
            
        print(v)	# Return modified size
	return len(v[:i - 1])
	
# Driver Code
if __name__ == '__main__':
	v = ["tom", "jerry", "jerry", "tom"]
	print(removeConsecutiveSame(v))
	
# This code is contributed by SHUBHAMSINGH10
