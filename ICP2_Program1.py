def string_alternative(full_name):
    return full_name[::2]

def full_name():
    f_name = input("Enter the first name: ")
    l_name = input("Enter the last name: ")

    full_name = f_name + " " + l_name
    print("Full Name: ", full_name)

    output_name = string_alternative(full_name)
    print("Output_Name: ", output_name)

if __name__ == "__main__":
    full_name()
