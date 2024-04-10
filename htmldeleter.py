# Removes lines
def remove_html_lines(html, start_line, end_line):
    lines = html.split('\n')
    cleaned_lines = []

    inside_block = False
    for line in lines:
        if start_line in line:
            inside_block = True
        elif end_line in line:
            inside_block = False
            continue
        
        if not inside_block:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

# Finds file and removes lines
def remove_from_file(file_path, start_line, end_line):
     # Read content from the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Remove HTML tags from the content
    clean_content = remove_html_lines(content, start_line, end_line)
    
    # Write the cleaned content back to the file
    with open(file_path, 'w') as file:
        file.write(clean_content)
    
    print("HTML code has been removed from the file.")


# Remove lines between start and end lines
if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    x = True
    while x == True:
        start_line = input("Enter the starting line to remove: ")
        end_line = input("Enter the ending line to remove: ")
        remove_from_file(file_path, start_line, end_line)
        another = input("Do you have more lines to remove? [y/n] ")
        if another == 'y':
            x = True
        else:
            x = False