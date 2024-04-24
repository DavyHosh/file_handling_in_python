def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Another line with some numbers: 98765\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation process completed.")


def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading process completed.")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("Appending another line.\n")
            file.write("Last line appended.\n")
        print("Content appended to file successfully.")
    except PermissionError:
        print("Permission denied. Unable to append to file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending process completed.")


def main():
    create_file()
    read_file()
    append_to_file()


if __name__ == "__main__":
    main()
