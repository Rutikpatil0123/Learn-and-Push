def get_middle_element(list):
    print(list[int(len(list) / 2)])


def get_min_and_max_elements(list):
    max_number = list[0]
    min_number = list[0]

    for i in range(1, int(len(list))):
        min_number = min(min_number, list[i])
        max_number = max(max_number, list[i])

    print(max_number, min_number)


def main():
    list = ["one", "Two", "Three", "Four", "Five"]
    get_middle_element(list)

    number_list = [98, 2, 4, 5, 1, 5, 6, 1233, 46, 45]
    get_min_and_max_elements(number_list)


if __name__ == "__main__":
    main()
