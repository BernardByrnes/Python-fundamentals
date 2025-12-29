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

# import json
# import csv
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# employee = {
#   "name": "Spongebob",
#   "age": 30,
#   "job": "cook"
# }

# employees = [["Name","Age","Job"],["Spongebob",30,"cook"],["Patrick",37,"Unemployed"],["sandy", 27, "Scientist"],]

# file_path = "C:/Users/Ben/Desktop/gif/python-tutorials/output.csv"

# try:
#     with open(file=file_path, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#           writer.writerow(row)
#           # file.write(employee + "\n")
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")

#~Reading Files

# file_path = "C:/Users/Ben/Desktop/gif/python-tutorials/output2.txt"

# try:
#     with open(file_path , mode='r') as file:
#           content = file.read()
#           print(content)
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")
# ==============================JSON==================================  # 
# import json

# file_path = "C:/Users/Ben/Desktop/gif/python-tutorials/output.json"

# try:
#     with open(file_path , mode='r') as file:
#           content = json.load(file)
#           print(content)
# except FileNotFoundError:
#   print("That file was not found")
# except PermissionError:
#   print("You do not have permission to read that file")
# ==============================CSV==================================  # 
import csv

file_path = "C:/Users/Ben/Desktop/gif/python-tutorials/output.csv"

try:
    with open(file_path , mode='r') as file:
          content = csv.reader(file)
          for line in content:
            print(line)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")