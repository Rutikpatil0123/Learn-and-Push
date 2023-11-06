def concatinate_string_from_list():
    list = ["Happy", "Diwali", "To", "All"]

    print(" ".join(list))


def convert_string_to_uppercase_and_lowercase(var):
    string1 = "FRewDsfseggre"

    if var:
        print(string1.upper())
    else:
        print(string1.lower())


def main():
    concatinate_string_from_list()
    convert_string_to_uppercase_and_lowercase(True)


if __name__ == "__main__":
    main()
