def main():
    file = open("file1.txt", "r")
    if file.mode == "r":
        contents = file.read()
        print(contents)

if __name__ == "__main__":
    main()
