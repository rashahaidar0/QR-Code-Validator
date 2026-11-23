from txtdata import TxtData
from helper import get_data, convert_date
class QRCode:
    """
    A class representing a QR Code.

    Attributes:
    - last_update_date (dict): Dictionary with keys
     'Day', 'Month', 'Year'.
    - owner (str): Owner of the QR code.
    - data (TxtData): The data contained in the QR code.
    - error_correction (float): The QR code's error correction level.
    """

    def __init__(self, file_path,
                 last_update_date="00/00/0000",
                 owner="Default Owner", error_correction=0.0):
        """
        (str, str, str, float) -> NoneType

        Initializes the QRCode object with 
        data from a file and metadata attributes.

        >>> q1 = QRCode("qrcode_binary.txt", "01/01/2024", "Vivian", 0.1)
        >>> q1.last_update_date['Day']
        '01'
        >>> q.owner
        'Vivian'
        >>> q2 = QRCode("qrcode_binary.txt", "15/08/2023", "Alex", 0.2)
        >>> q2.last_update_date['Month']
        '08'
        >>> q2.error_correction
        0.2
        >>> q3 = QRCode("qrcode_binary.txt", "31/12/2022", "Jamie", 0.0)
        >>> q3.last_update_date['Year']
        '2022'
        >>> q3.owner
        'Jamie'
        """
        # Use the helper function to get 
        # the 2D list and wrap it in TxtData object
        self.data = TxtData(get_data(file_path))
        # Use the helper function to convert 
        # and store the string date into dict 
        self.last_update_date = convert_date(last_update_date)
        # Store the owner name and the error correction level
        self.owner = owner
        self.error_correction = error_correction
    
    def __str__(self):
        """
        () -> str

        Returns a string describing the QRCode object in the expected format.

        >>> q1 = QRCode("qrcode_binary.txt", "01/01/2024", "Vivian", 0.1)
        >>> print(q1)
        The QR code was created by Vivian and last updated in 2024.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        >>> q2 = QRCode("qrcode_binary.txt", "15/08/2023", "Alex", 0.0)
        >>> print(q2)
        The QR code was created by Alex and last updated in 2023.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        >>> q3 = QRCode("qrcode_binary.txt", "31/12/2022", "Jamie", 0.2)
        >>> print(q3)
        The QR code was created by Jamie and last updated in 2022.
        The details regarding the QR code file are as follows:
        This TxtData object has 33 rows and 33 columns.
        """
        return ("The QR code was created by " + self.owner + 
                " and last updated in " + 
                self.last_update_date['Year'] + ".\n" +
                "The details regarding the QR code file are as follows:\n" +
                "This TxtData object has " + 
                str(self.data.rows) + " rows and " + 
                str(self.data.cols) + " columns.")
    
    def equals(self, other):
        """
        (QRCode) -> bool

        Returns True if the data and error 
        correction level of both QR codes match.

        >>> q1 = QRCode("qrcode_binary.txt", "01/01/2024", "A", 0.1)
        >>> q2 = QRCode("qrcode_binary.txt", "05/01/2024", "B", 0.1)
        >>> q1.equals(q2)
        True
        >>> q3 = QRCode("qrcode_binary.txt", "01/01/2024", "A", 0.2)
        >>> q1.equals(q3)
        False
        >>> my_qrcode = QRCode("qrcode_binary.txt", 
                               "01/09/2024", "Vivian", 0.1)
        >>> my_qrcode_copy = QRCode("qrcode_binary_copy.txt", "01/09/2022",
                                    "Xuanpu", 0.1)
        >>> my_qrcode.equals(my_qrcode_copy)
        True
        """
        # Compare both QRCode data and 
        # both of their error correction value, 
        # return true if it is the same for both 
        return (self.data.equals(other.data) and 
                self.error_correction == other.error_correction)
    
    def is_corrupted(self, precise_qrcode):
        """
        (QRCode) -> bool

        Returns True if the QRCode object's data differs
        from the precise QRCode beyond the allowed error correction.

        >>> q1 = QRCode("qrcode_binary.txt", "01/01/2024", "A", 0.1)
        >>> q2 = QRCode("qrcode_binary.txt", "01/01/2024", "A", 0.1)
        >>> q1.is_corrupted(q2)
        False
        >>> q3 = QRCode("corrupted_qr.txt", "01/01/2024", "A", 0.1)
        >>> q3.is_corrupted(q2)
        True
        >>> my_qrcode = QRCode("qrcode_binary.txt", "01/09/2024",
                               "Vivian", 0.1)
        >>> my_c_qrcode = QRCode("qrcode_binary_c.txt",
                                 "01/09/2000", "Vivian", 0.1)
        >>> my_c_qrcode.is_corrupted(my_qrcode)
        True    
        """
        # Determine if the data is corrupted by comparing data with allowed 
        # error correction, return True if it is corrupted
        return not self.data.approximately_equals(
            precise_qrcode.data, precise_qrcode.error_correction)
