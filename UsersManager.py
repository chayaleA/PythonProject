from functools import reduce
import os
import re


# Bonus 5% - I read the instructions out loud (even though I did the project alone....).

# ---------------------------------------------------Task 8---------------------------------------------------

# class for Task 8 ex 3
class SophisticatedArray:
    __slots__ = ['user_names']

    def __init__(self):
        self.user_names = []

    def read_user_names(self, user_names):
        self.user_names = user_names

    def exclude_first_10_percent(self):
        num_to_exclude = int(0.1 * len(self.user_names))
        self.user_names = self.user_names[num_to_exclude:]


# Task 8 ex 1
def check_and_create_file(file_path):
    """
        Check if a file exists at the specified path. If not, create the file and its directory.
        Parameters:
            - file_path (str): The path to the file to be checked or created.
    """
    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        with open(os.path.join("DataFiles", os.path.basename(file_path)), 'w'):
            pass
    else:
        print(f"File '{file_path}' already exists. Reading its contents:")
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            print(file_contents)
            return file_contents


# Task 8 ex 2
def read_user_names(file_path):
    """
    Read the names of users from the file into a generator.

    Parameters:
        file_path (str): The path to the file containing user names.

    Yields:
        str: A user name read from the file.
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


# Task 8 ex 3
def exclude_first_10_percent(names):
    """
       Exclude the first 10% of names from the input list.

       Parameters:
           names (list): A list of user names.

       Returns:
          A list whithout 10% names
    """

    sophisticated_array = SophisticatedArray()
    sophisticated_array.read_user_names(names)
    sophisticated_array.exclude_first_10_percent()
    return sophisticated_array.user_names


# Task 8 ex 4
def users_in_even_rows(users):
    """
      Exclude users that are in even-numbered rows (0-indexed) from the input list.

      Parameters:
          users (list): A list of user names.

      Returns:
           A list whithout 10% names from the even rows
    """
    even_users = list(filter(lambda x: users.index(x) % 2 != 0, users))
    sophisticated_array = SophisticatedArray()
    sophisticated_array.read_user_names(even_users)
    sophisticated_array.exclude_first_10_percent()
    return sophisticated_array.user_names


# Task 8 ex 5
def validate_email_address(email):
    """
       Validate whether an email address follows a standard pattern.

       Parameters:
           email (str): The email address to validate.

       Returns:
           bool: True if the email address is valid, False otherwise.
    """
    pattern = r'^$|^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# Task 8 ex 5
def validate_addresses():
    """
       Validate email addresses read from a file and print the result.

       Returns:
           list: A list of invalid email addresses.
    """

    invalid_emails = []
    with open("DataFiles/UsersEmail.txt", "r") as file:
        emails = [line.strip() for line in file]
        invalid_emails = [email for email in emails if not validate_email_address(email)]
    if len(invalid_emails) == 0:
        print("Allright emails")
    else:
        print("There are some invalid emails")
        for email in invalid_emails:
            print(email)
    return invalid_emails

# Task 8 ex 6
def filter_gmail_addresses():
    """
        Filter out Gmail addresses from a list of email addresses read from a file.

        Returns:
            list: A list of filtered email addresses.
    """
    pattern = r'^\S+@gmail\.com$'
    with open("DataFiles/UsersEmail.txt", "r") as file:
        emails = file.readlines()
    return [email.strip() for email in emails if email.strip() and re.match(pattern, email.strip())]


# Task 8 ex 7
def check_email_username_correspondence(emails, names):
    """
    Check if each name is contained in the corresponding email address using reduce.

    Parameters:
        - emails (list): A list of email addresses.
        - names (list): A list of names.

    Returns:
        - dict: A dictionary where the keys are email addresses and the values indicate whether the email address
                consists of the corresponding username.
    """

    def check_username_in_email(correspondence, pair):
        email, name = pair
        correspondence[f"{name} - {email}"] = name.strip() in email.strip()
        return correspondence

    return reduce(check_username_in_email, zip(emails, names), {})

def format_user_name(name):
    """
        Convert a user name into a string of ASCII codes separated by spaces.

        Parameters:
            name (str): The user name to convert.

        Returns:
            str: A string of ASCII codes.
    """
    return ' '.join(str(ord(char)) for char in name)


def convert_ascii_to_str(ascii_string):
    """
        Convert a string of ASCII codes separated by spaces into a string of characters.

        Parameters:
            ascii_string (str): The string of ASCII codes.

        Returns:
            str: The converted string.
    """
    return ''.join(chr(int(code)) for code in ascii_string.split())


# Task 8 ex 8
def check_name_in_list(name, user_list):
    """
        Check if a given name is present in a list of user names.

        Parameters:
            name (str): The name to check.
            user_list (list): A list of user names.

        Returns:
            tuple: A tuple containing a boolean indicating name presence and an integer indicating the count of 'A' in the name.
    """
    user_list_cleaned = [user_name.strip() for user_name in user_list]
    name_present = name in user_list_cleaned
    formatted_name = format_user_name(name)
    formatted_name = convert_ascii_to_str(formatted_name)
    count_A = sum(1 for char in name if char == 'A')
    return name_present, count_A


# Task 8 ex 9
def check_names(names):
    """
       Check if all names in the list start with a capital letter.

       Parameters:
           names (list): A list of names.

       Returns:
           bool: True if all names start with a capital letter, False otherwise.
    """
    list_names = [name for name in names]
    return all(name.istitle() for name in list_names)


# Task 8 ex 10
def compute_sum(numbers_list):
    """
      Compute the sum based on a list of numbers.

      Parameters:
          numbers_list (list): A list of numbers.

      Returns:
          int: The computed sum.
    """
    return sum(number // 8 * 200 + number % 8 * 50 for number in numbers_list)

#-------------------------init---------------------------

with open("DataFiles/UsersEmail.txt", "r") as file:
    emails = file.readlines()

with open("DataFiles/UsersName.txt", "r") as file:
    names = file.readlines()

# Task 8 ex 1
users_names = check_and_create_file("DataFiles/UsersName.txt")
file_path = "DataFiles/UsersName.txt"

# Task 8 ex 2
for user_name in read_user_names(file_path):
    print(user_name)

# Task 8 ex 3
print(exclude_first_10_percent(names))

# Task 8 ex 4
print(users_in_even_rows(names))

# Task 8 ex 5
invalid_emails = validate_addresses()
for email in invalid_emails:
    print(email)

# Task 8 ex 6
print("Gmail addresses:")
filtered_gmails = filter_gmail_addresses()
print("Filtered Gmail addresses:", filtered_gmails)

# Task 8 ex 7
check = check_email_username_correspondence(emails, names)
print("check_email_username_correspondence:")
print(check)

# Task 8 ex 8
name_present, count_A = check_name_in_list('Chana', names)
print("Checking if 'Chana' is in the list:", name_present)
print(f"Amount of the char A in the name is: {count_A}")

# Task 8 ex 9
print(f"All the names begin with capital letter: {check_names(names)}")

# Task 8 ex 10
payment_list = [15, 20, 76, 88, 4, 43, 19, 5, 9]
print("Total Payment from Customers:", compute_sum(payment_list))


