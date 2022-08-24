
def file_not_found_error():
    try:
        file = open("a_file.txt")

        a_dict = {"key": "value"}
        print(a_dict['non_existent_key'])

    except FileNotFoundError:
        # File Not Found
        with open("a_file.txt", "w") as file:
            file.write("File Not Found.")

    except KeyError as error_msg:
        # KeyError        
        a_dict['non_existent_key'] = f"That key {error_msg} does not exist."
        print(a_dict['non_existent_key'])

    else:
        content = file.read()
        print(content)
    finally:
        file.close()


def bmi_calculator():
    # ValueError
    height = float(input("Height : "))
    weight = int(input("Weight : "))

    try:
        if height > 3:
            raise ValueError("Human Height should not be over 3 meters.")
        else:
            bmi = weight / height ** 2
    except ValueError as error:
        print(error)
    else:            
        print(bmi)


def pie_make(index):
    # IndexError
    fruit_list = ["Apple", "Banana", "Pear"]

    try:
        fruit = fruit_list[index]
    except IndexError:
        print("Fruit Pie.")
    else:
        print(f"{fruit} Pie.")


# TypeError
# tax = "7"
# total = (150 * tax) / 100


if __name__ == "__main__":
    # file_not_found_error()
    bmi_calculator()
    # pie_make(4)