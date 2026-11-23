from copy import deepcopy

class TxtData:
    """
    A class to represent a 2D binary data file loaded into a nested list.

    Attributes:
    - data (list of list of int): Nested list holding the binary data.
    - rows (int): Number of rows in the data.
    - cols (int): Number of columns in the data.
    """

    def __init__(self, data):
        """
        (list of list of int) -> NoneType

        Initializes the TxtData object with a deep copy 
        of data the 2D list inputed, 
        and stores the number of rows and columns. 

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> t1.rows
        2
        >>> t1.cols
        2
        >>> t1.data
        [[0, 1], [1, 0]]
        >>> t2 = TxtData ([0])
        >>> t2.rows
        1
        >>> t2.cols
        1
        >>> t3 = TxtData ([[1, 1, 1], [0, 0, 0]])
        >>> t3.cols
        3
        """
        # Creata a deep copy of the input data of the 2D list
        self.data = deepcopy(data)
        # Store number of rows and columns 
        self.rows = len(data)
        self.cols = len(data[0])
        
        
    def __str__(self):
        """
        () -> str

        Returns a string describing the
        number of rows and columns of the TxtData object.

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> print(t1)
        This TxtData object has 2 rows and 2 columns.
        >>> t2 = TxtData ([0])
        >>> print(t2)
        This TxtData object has 1 rows and 1 columns.
        >>> t3 = TxtData ([[1, 1, 1], [1, 1, 1]])
        >>> print (t3)
        This TxtData object has 2 rows and 3 columns. 
        """
        return ("This TxtData object has " + str(self.rows) + " rows and " + 
                str(self.cols) + " columns.")
        
    def get_pixels(self):
        """
        () -> int

        Returns the total number of 
        pixels (rows * columns) in the TxtData object.

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> t1.get_pixels()
        4
        >>> t2 = TxtData([[1]])
        >>> t2.get_pixels()
        1
        >>> t3 = TxtData([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        >>> t3.get_pixels()
        9
        """
        return self.rows * self.cols
    
    def get_data_at(self, row, col):
        """
        (int, int) -> int

        Returns the integer in the data at the given row and column.
        Raises a ValueError if the row or column index is out of bound.

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> t1.get_data_at(0, 1)
        1
        >>> t2 = TxtData([[0]])
        >>> t2.get_data_at(0, 0)
        0
        >>> t3 = TxtData([[1, 1], [0, 0]])
        >>> t3.get_data_at(2, 0)
        Traceback (most recent call last):
        ValueError: Index out of bound!

        """
        # Check if the given row and column are within the bounds
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Index out of bound!")
        # Return the value at the given index of the row and column 
        return self.data[row][col]
    
    def pretty_save(self, file_name):
        """
        (str) -> NoneType

        Writes a formatted version of the data to the specified file.
        Converts 1s to  ”\u2588” and 0s to "  " for QR code visualization.
        Does not return anything.

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> t1.pretty_save("output1.txt")
        >>> t2 = TxtData([[1, 0, 1]])
        >>> t2.pretty_save("output2.txt")
        >>> my_list = get_data("qrcode_binary.txt")
        >>> my_txt = TxtData(my_list)
        >>> my_txt.pretty_save("qrcode_pretty.txt")
        """
        block = "\u2588"
        # Open the file to write in it 
        fobj = open(file_name, "w")
        # Write each line based on the given binary data
        for row in self.data:
            line = ""
            for value in row:
                if value == 1:
        # The number one should be represented with 2 blocks
                    line += block * 2
                else:
        # The number 0 should be represented with 2 spaces
                    line += "  "
        # Write the formatted line after it 
        # has just been modified above into the file
            fobj.write(line + "\n")
        # Close the file 
        fobj.close()
    
    def equals(self, other):
        """
        (TxtData) -> bool

        Returns True if the current TxtData 
        object has the same data as another TxtData object.

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> t2 = TxtData([[0, 1], [1, 0]])
        >>> t1.equals(t2)
        True
        >>> t3 = TxtData([[1, 1], [1, 0]])
        >>> t1.equals(t3)
        False
        >>> my_list_simple = [[1,2,3],[4,5,6]]
        >>> my_txt_simple_1 = TxtData(my_list_simple)
        >>> my_txt_simple_2 = TxtData(my_list_simple)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        True
        """
        # Compare the 2D lists of both TxtData objects
        return self.data == other.data
    
    def approximately_equals(self, other, precision):
        """
        (TxtData, float) -> bool

        Returns True if the fraction of different values 
        between the two TxtData objects is less than or equal to precision.

        >>> t1 = TxtData([[0, 1], [1, 0]])
        >>> t2 = TxtData([[0, 1], [0, 0]])
        >>> t1.approximately_equals(t2, 0.25)
        True
        >>> t1.approximately_equals(t2, 0.1)
        False
        >>> t3 = TxtData([[9, 9], [9, 9]])
        >>> t4 = TxtData([[9, 9], [9, 8]])
        >>> t3.approximately_equals(t4, 0.2)
        True
        >>> my_list_simple_1 = [[1,2,3],[4,5,6]]
        >>> my_list_simple_2 = [[1,2,3],[7,8,9]]
        >>> my_txt_simple_1 = TxtData(my_list_simple_1)
        >>> my_txt_simple_2 = TxtData(my_list_simple_2)
        >>> my_txt_simple_1.equals(my_txt_simple_2)
        False
        >>> my_txt_simple_1.approximately_equals(my_txt_simple_2, 0.5)
        True
        """
        # Check if the values are the same, return False if they aren't
        if self.rows != other.rows or self.cols != other.cols:
            return False

        # Total number of elements to compare 
        # and counter that gives the number of 
        # elements that are different from each other
        total = self.get_pixels()
        diff = 0
        # Count how many elements differ from each other 
        # between the two given data sets
        for r in range(self.rows):
            for c in range(self.cols):
                if self.data[r][c] != other.data[r][c]:
                    diff += 1
        # Return True if the proportion of
        # differing pixels is within the allowed precision
        return (diff / total) <= precision

