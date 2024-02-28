def main():
    with open("diary.txt") as my_file:
        entries = my_file.read()
    while True:
        operation = input("1 - add an entry, 2 - read entries, 0 - quit\nFunction:")
        if operation == "1":
            content = input("Diary entry: ")
            with open("diary.txt","a") as diary:
                diary.write(f"{content}\n")
            print("Diary saved\n")
        elif operation == "2":
            print("Entries: ")
            with open("diary.txt") as diary:
                for row in diary:
                    print(row)
        elif operation == "0":
            print('Bye now!'+"\n")
        break

main()