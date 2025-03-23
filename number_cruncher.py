def process_numbers():

    total = count = 0
    minimum = None
    maximum = None

    try:
        with open("numbers.txt", "r") as infile, open("error_log.txt", "w") as error_log:

            line_number = 1

            for line in infile:
                try:
                    # Convert each line from a string to a floating number
                    number = float(line.strip())

                    # Calculate Sum
                    total += number

                    # Calculate Count
                    count += 1

                    # Calculate Average
                    if count > 0:
                        average = total / count
                    else:
                        average = 0
                    
                    # Calculate Minimum
                    if minimum is None or number < minimum:
                        minimum = number

                    # Calculate Maximum
                    if maximum is None or number > maximum:
                        maximum = number

                except ValueError:
                    error_log.write(f"Line {line_number} contains a non-numeric value: '{line.strip()}'\n")

                line_number += 1

        with open("report.txt", "w") as report:
            report.write("Report:\n")
            report.write("---------\n")
            report.write(f"Sum: {total}\n")
            report.write(f"Count: {count}\n")
            report.write(f"Average: {average}\n")
            report.write(f"Minimum: {minimum}\n")
            report.write(f"Maximum: {maximum}\n")
            
    except FileNotFoundError:
        print("Error: 'numbers.txt' not found. Please create the file with numbers.")
    except ValueError as e:
        print("Error: Found a non-numeric value. Please ensure all lines contain valid numbers.")
    finally:
        print("File processing complete.")
        
if __name__ == "__main__":
    process_numbers()