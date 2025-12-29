txt_data = "i like Watermelon"

file_path = "output.txt"


with open(file=file_path, mode="w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")