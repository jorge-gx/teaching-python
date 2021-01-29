# open a file named sample.txt and write to it

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# using context manager
# with open()
# allows us to allocate and release resources
# no need to use file.close()

with open("sample.txt", 'w', encoding='utf-8') as file:
    file.write("Writing this line in the file.\n")
    file.write("Now we'll write some values:\n")
    for number in numbers:
        file.write(f"number = {number}\n")
    file.write("The end.")
