import sqlparse

def remove_data_insertion(parsed_statements):
    filtered_statements = []
    for statement in parsed_statements:
        if not statement.get_type() == 'INSERT':
            filtered_statements.append(statement)
    return filtered_statements

def extract_database_structure(input_file, output_file):
    with open(input_file, 'r') as f:
        sql_content = f.read()

    # Parse the SQL content using sqlparse
    parsed_statements = sqlparse.parse(sql_content)

    # Remove data insertion statements
    parsed_statements = remove_data_insertion(parsed_statements)

    # Write the structure-only SQL content to a new file
    with open(output_file, 'w') as f:
        for statement in parsed_statements:
            f.write(str(statement) + '\n')

# Example usage:


input_file_path = r"D:\monymovment\Cashflows\DATABASE\backup\lastbackup_copy.sql"
output_file_path =r"D:\monymovment\Cashflows\DATABASE\backup\lastbackup_copy_copy.sql"

extract_database_structure(input_file_path, output_file_path)

