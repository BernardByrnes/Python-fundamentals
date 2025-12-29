import numpy as np

# my_list= [1,2,3,4]

# my_list = my_list * 2

# print(my_list)

# ==================================

# array = np.array([1,2,3,4,])

# array = array*10

# print(array)

# ====================================
# array = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
#                   [["J","K","L"],["M","N","O"],["P","Q","R"]],
#                   [["S","T","U"],["V","W","X"],["Y","Z","_"]]])

# # print(array.ndim)
# # print(array.shape)
# # print(array[0,1,1])

# word = array[0,0,2] + array[2,0,2] + array[1,2,0]
# print(word)

# ====================ROW AND COLUMN SELECTION=====================================

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array[start:end:step]
# print(array[0:4:2])
# print(array[::2])
# print(array[::-1])


#columns 
# print(array[:,0])
# print(array[:,-2])
# print(array[:,1:4])
# print(array[:,1:])
# print(array[:, ::2])

#ROWS AND COLUMNS
# print(array[0:2,0:2]) 
# print(array[0:2,2:]) 
# print(array[2:4,2:]) 

