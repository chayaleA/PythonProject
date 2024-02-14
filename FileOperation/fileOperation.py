import datetime
import pandas as pd
import docx
class FileOperation:

    # Task 1 ex 1
    def read_excel(self, file_path: str):
        """
           Read data from an Excel file located at the specified file path.

           Parameters:
                - data: file_path (string): The path to the Excel file

           Returns:
               - DataFrame: The data read from the Excel file

           """
        try:
            data = pd.read_excel(file_path)
            return data

        except FileNotFoundError:
            print(f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}>"
                  f" Error: File '{file_path}' not found. <Chaya>")
            return None

        except Exception as e:
            print(f"Error! reading Excel file: {e}")
            return None

    # Task 1 ex 2
    def save_to_excel(self, data, file_name: str):
        """
        Save the provided data to a new Excel file with the given file name.

        Parameters:
            - data: The data to be saved to the Excel file.
            - file_name (string): The name of the Excel file to be saved.

        Returns:
            - bool: True if the file was saved successfully, False otherwise.
        """
        try:
            data.to_excel(file_name, index=False)
            print(
                f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}>"
                f" data successfully saved to '{file_name}'. <Chaya>")
            return True

        except Exception as e:
            print(f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}>"
                  f" Error saving data to Excel file: {e} <Chaya>")
            return False

    # Task 7 ex 2
    def read_file(self, file_path):
        """
        Read data from a file.

        Parameters:
            file_path (str): The path to the file.

        Returns:
            DataFrame: A pandas DataFrame containing the data from the file.
        """
        read_functions = {
            'csv': pd.read_csv,
            'xls': pd.read_excel,
            'xlsx': pd.read_excel,
            'json': pd.read_json,
            'docx': self.read_word_file,
            'doc': self.read_word_file
        }
        try:
            # Determine the file type based on its extension
            file_extension = file_path.split('.')[-1].lower()

            if file_extension in read_functions:
                read_function = read_functions[file_extension]
                data = read_function(file_path)
                return data
            else:
                print("Unsupported file type")
                return None
        except Exception as e:
            print(f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}>"
                  f" Error: '{e}' <Chaya>")
            return None

    def read_word_file(self, file_path):
        """
        Read text from a Word document.

        Parameters:
            file_path (str): The path to the Word document.

        Returns:
            str: The text content of the Word document.
        """
        try:
            doc = docx.Document(file_path)
            full_text = []
            for paragraph in doc.paragraphs:
                full_text.append(paragraph.text)
            return '\n'.join(full_text)
        except Exception as e:
            print(f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}>"
                  f" Error: '{e}' <Chaya>")
            return None
