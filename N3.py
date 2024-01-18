def convert_heights_nested(h_inches):
    h_centimeters = []

    for inch in h_inches:
        cm = round(inch * 2.54, 2)
        h_centimeters.append(cm)

    return h_centimeters

def convert_heights_comprehension(h_inches):
    h_centimeters = [round(inch * 2.54, 2) for inch in h_inches]

    return h_centimeters

def main():
    h_inches = []
    num_customers = int(input("Enter the number of customers: "))

    for i in range(num_customers):
        height = float(input(f"Enter height for customer {i+1} in inches: "))
        h_inches.append(height)

    h_centimeters_nested = convert_heights_nested(h_inches)
    print("Heights in centimeters using Nested Loop:", h_centimeters_nested)

    h_centimeters_comprehension = convert_heights_comprehension(h_inches)
    print("Heights in centimeters using List Comprehension:", h_centimeters_comprehension)

if __name__ == "__main__":
    main()
