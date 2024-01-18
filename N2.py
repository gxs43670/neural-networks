def count_words(line):
    word_count = {}
    words = line.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def process_and_store_output(lines):
    output_lines = []

    for line in lines:
        output_lines.append(line.strip())
        word_count = count_words(line)
        
        # Include word count for each line
        output_lines.append("Word_Count:")
        for word, count in word_count.items():
            output_lines.append(f"{word}: {count}")

    return output_lines

def main():
    # Read input from file
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Process and store the output
    output_lines = process_and_store_output(lines)

    # Print the output
    for output_line in output_lines:
        print(output_line)

    # Write the output to output.txt
    with open("output.txt", "w") as output_file:
        output_file.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
