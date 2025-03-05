import csv

def csv_to_sql_insert(csv_file_path, table_name):
    # Open the CSV file
    with open(csv_file_path, mode='r') as file:
        # Read the CSV file
        csv_reader = csv.reader(file)
        
        # Get the header (column names)
        headers = next(csv_reader)
        
        # Initialize a list to store the SQL commands
        sql_commands = []
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Create the SQL INSERT INTO command
            sql_command = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join([f'\"{value}\"' for value in row])});"
            # Add the SQL command to the list
            sql_commands.append(sql_command)
    
    return sql_commands

# Example usage
csv_file_path = 'titles.csv'
table_name = 'my_table'
sql_commands = csv_to_sql_insert(csv_file_path, table_name)

# Write the SQL commands to a file
with open('insert_commands.sql', mode='w') as file:
    for command in sql_commands:
        file.write(command + '\n')

print("SQL commands have been written to insert_commands.sql")