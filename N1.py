def fullname(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name

def string_alternative(full_name):
    return full_name[::2]

def main():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")

    full_name = fullname(f_name, l_name)
    print("Full name:", full_name)

    alternate_chars = string_alternative(full_name)
    print("Alternate characters in the full name:", alternate_chars)

if __name__ == "__main__":
    main()
