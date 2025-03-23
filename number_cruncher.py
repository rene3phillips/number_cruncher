def process_numbers():

    total = count = 0
    minimum = None
    maximum = None

    try:
        with open("numbers.txt", "r") as infile:
            for line in infile:

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

        with open("report.txt", "w") as outfile:
            outfile.write("Report:\n")
            outfile.write("---------\n")
            outfile.write(f"Sum: {total}\n")
            outfile.write(f"Count: {count}\n")
            outfile.write(f"Average: {average}\n")
            outfile.write(f"Minimum: {minimum}\n")
            outfile.write(f"Maximum: {maximum}\n")
            
    except FileNotFoundError:
        print("Error: 'numbers.txt' not found. Please create the file with numbers.")
    except ValueError as e:
        print("Error: Found a non-numeric value. Please ensure all lines contain valid numbers.")
    finally:
        print("File processing complete.")
        
if __name__ == "__main__":
    process_numbers()