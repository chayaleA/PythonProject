from fileOperation import *

def main():
    # create an instance of fileOperation class
    file_op = FileOperation()

    # Task 7 ex 2
    csv_content = file_op.read_file("../DataFiles/example.csv")
    word_content = file_op.read_file("../DataFiles/example.docx")

    # Task 1 ex 1
    excel_content = file_op.read_excel("../DataFiles/output.xlsx")
    print(csv_content)
    print(word_content)
    print(excel_content)

    # Task 1 ex 2
    file_op.save_to_excel(excel_content, "../DataFiles/save.xlsx")

    # read data from file
    yafeNof_data = file_op.read_file("../DataFiles/YafeNof.csv")
    print("Data read from YafeNof file:")
    print(yafeNof_data)

    # save data to a new Excel file
    data_to_save = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
    file_op.save_to_excel(data_to_save, '../DataFiles/output.xlsx')

if __name__ == "__main__":
    main()
