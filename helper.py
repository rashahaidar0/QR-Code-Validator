def convert_date(date_str):
    """
    (str) -> dict
    
    Converts a date in the format 'dd/mm/yyyy' to a dictionary
    with 'day', 'month', and 'year' keys.
    Returns None if the format is incorrect or values are invalid.
    
    >>> convert_date("25/12/2020")
    {'day': 25, 'month': 12, 'year': 2020}
    >>> convert_date("01/01/1999")
    {'day': 1, 'month': 1, 'year': 1999}
    >>> convert_date("30-02-2020")
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    """
    # Make sure the length of the input string 
    if len(date_str) != 10:
        raise ValueError("Input format incorrect!")
    # Check if format is correct: dd/mm/yyyy
    if date_str[2] != '/' or date_str[5] != '/':
        raise ValueError("Input format incorrect!")
    
    # Get the day, month and year substrings
    day_str = date_str[0:2]
    month_str = date_str[3:5]
    year_str = date_str[6:]
    
    # Manually check if all characters are digits
    for ch in day_str + month_str + year_str:
        if ch < '0' or ch > '9':
            raise ValueError("Input format incorrect!")
    
    # Convert to integer
    day_int = int(day_str)
    month_int = int(month_str)
    year_int = int(year_str)
    
    if day_int < 1 or day_int > 31:
        raise ValueError("Input format incorrect!")
    if month_int < 1 or month_int > 12:
        raise ValueError("Input format incorrect!")
    if year_int < 1:
        raise ValueError("Input format incorrect!")
    
    # Return the dictionary with the components
    return {'Day': day_str, 'Month': month_str, 'Year': year_str}

def get_data(file_path):
    """
    (str) -> list
    
    Reads a file at the given path and returns 
    a 2D list of integers (0 or 1) based on file contents.
    Raises a ValueError if any character in the file is not '0' or '1'.
    
    >>> get_data("sample_qr.txt")
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    >>> get_data("test.txt")
    [[1, 0], [0, 1]]
    >>> get_data("empty.txt")
    []
    >>> get_data("small_data_error.txt")
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!
    """
    result = []
    # Open the file and read it 
    fobj = open(file_path, 'r')
    
    for line in fobj:
        row = []
    # Go through each character in the line, raise 
    # an error on invalids characters and avoid empty rows
        for char in line:
            if char == '0':
                row.append(0)
            elif char == '1':
                row.append(1)
            elif char != '\n':
                fobj.close()
                raise ValueError("File should contain only 0s and 1s!")
        if row != []:
            result.append(row)
    
    # Close the file
    fobj.close()
    return result
