# txt_data = "i like Watermelon"

# file_path = "output.txt"


# with open(file=file_path, mode="w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")
# =================================================================
# txt_data = "i like Watermelon!"
# txt_data2 = "i also like Oranges!"

# file_path = "C:/Users/Ben/Desktop/gif/python-tutorials/output2.txt"

# try:
#     with open(file=file_path, mode="a") as file:
#         file.write("\n" + txt_data2)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")

# ======================================================================

import json
import csv
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# employee = {
#   "name": "Spongebob",
#   "age": 30,
#   "job": "cook"
# }

employees = [[],[],[],[],]

file_path = "C:/Users/Ben/Desktop/gif/python-tutorials/output.json"

try:
    with open(file=file_path, mode="w") as file:
        json.dump(employee,file, indent=4)
          # file.write(employee + "\n")
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")