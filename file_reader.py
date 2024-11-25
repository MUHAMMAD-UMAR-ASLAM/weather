import csv
def read_file(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = [] 
            for row in reader:
                rows.append(row)
            
            return rows
    except FileNotFoundError:
        return f"Error: The file at {file_path} does not exist."
    except IOError:
        return "Error: There was an issue reading the file."

