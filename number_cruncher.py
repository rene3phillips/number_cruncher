def process_numbers():

    total = count = average = 0
    minimum = None
    maximum = None

    while True:

        file_name = input("\nEnter the name of a file you would like processed: ").strip()

        try:
            with open(file_name, "r") as infile, open("error_log.txt", "w") as error_log:

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
            print(f"Error: '{file_name}' not found.")
            
        finally:
            if count > 0:
                print("File processing complete.\n")
                break
            else:
                print("There was no valid data to process.")
        
if __name__ == "__main__":
    process_numbers()