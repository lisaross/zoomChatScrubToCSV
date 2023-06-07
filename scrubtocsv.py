import re
import sys
import csv
import os

def parse_line(line):
    # Split the line into timestamp, rest
    timestamp, rest = line.split('From', 1)
    message = re.search(r".*:(.*)", rest)
    
    # Check if there's a message
    if message:
        message = message.group(1).strip()
    else:
        message = ''
    
    # Return as a dictionary
    return timestamp.strip(), message.strip()

def convert_file_to_csv(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = f.readlines()
    
    # Create a temporary csv file
    temp_file = input_file_name.rsplit('.', 1)[0] + '_temp.csv'
    output_file = input_file_name.rsplit('.', 1)[0] + '.csv'
    
    # Open the output file in write mode
    with open(temp_file, 'w', newline='') as f:
        fieldnames = ['timestamp', 'message']
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        writer.writeheader()
        
        timestamp = message = ''
        messages = []
        for line in lines:
            if 'From' in line:
                # If we have a message, write it to the CSV
                if messages:
                    writer.writerow({'timestamp': timestamp, 'message': ' '.join(messages).strip()})
                    messages = []
                
                # Parse the new line
                timestamp, message = parse_line(line)
                messages.append(message)
            elif line.strip():
                # Append the line to the last message
                messages.append(line.strip())
        
        # Write the last message
        if messages:
            writer.writerow({'timestamp': timestamp, 'message': ' '.join(messages).strip()})

    os.remove(input_file_name)
    os.rename(temp_file, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrubnames.py <filename>")
        sys.exit(1)

    file_name = sys.argv[1]
    convert_file_to_csv(file_name)
