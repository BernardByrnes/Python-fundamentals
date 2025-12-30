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

# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])

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

#~Arithmetic
#^scalar arithmetic

# array = np.array([1,2,3,4])
# array2 = np.array([1.4,2.7,3.3,4.7])

# print(array + 2)
# print(array * 2)
# print(array / 3)
# print(array ** 5)


#^Vectorized math func

# print(np.sqrt(array))
# print(np.round(array2))
# print(np.floor(array2))
# print(np.ceil(array2))
# print(np.pi)

# radii = np.array([1,2,3])
# print(np.pi * (radii ** 2))

#^Element-wise arithmetic

# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2)

# scores = np.array([92,94,84,100,30 ,50, 72,68])
# scores[scores<60]=0

# print(scores)

# print(scores > 90)
# print(scores < 70)

#~broadcasting
# array4 = np.array([[1,2,3,4]])
# array5 = np.array([[1],[2],[3],[4]])

# print(array4.shape)
# print(array5.shape)

# print(array4 * array5)

#~aggregation functions

# array3= np.array([[1,2,3,4,5],
#           [6,7,8,9,10]])

# print(np.sum(array3))
# print(np.mean(array3))
# print(np.std(array3))
# print(np.var(array3))
# print(np.min(array3))
# print(np.max(array3))
# print(np.argmax(array3))

#print(np.sum(array3, axis=0)) #sum all the columns
#print(np.sum(array3, axis=1)) #sum all the rows

#~FILTERING

ages = np.array([[21,17,19,23,19,30,20],
                [30,15,16,17,19,20,30]])

teenagers = ages[ages<20]
adults = ages[(ages>=18) & (ages <65)]
kids = ages[ages<18]
evens = ages[ages % 2 ==0]

# print(teenagers)
# print(adults)
print(kids)
print(evens)