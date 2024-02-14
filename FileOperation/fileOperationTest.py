import unittest
import warnings
import pandas as pd
from fileOperationMain import FileOperation

class FileOperationTest(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        self.file_op = FileOperation()

    def test_read_file(self):
        # Test reading an existing file
        file_path = "../DataFiles/YafeNof.csv"
        data = self.file_op.read_file(file_path)
        self.assertIsInstance(data, pd.DataFrame)

        # Test reading a non-existing Excel file
        non_existing_file_path = '../DataFiles/non_existing_file.xlsx'
        data = self.file_op.read_file(non_existing_file_path)
        self.assertIsNone(data)

    def test_save_to_excel(self):
        # Test saving data to a new Excel file
        data_to_save = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
        file_name = '../DataFiles/test_output.xlsx'
        result = self.file_op.save_to_excel(data_to_save, file_name)
        self.assertTrue(result)

        # Test saving data with an existing file name (should overwrite)
        data_to_save = pd.DataFrame({'Column1': [4, 5, 6], 'Column2': ['D', 'E', 'F']})
        result = self.file_op.save_to_excel(data_to_save, file_name)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
