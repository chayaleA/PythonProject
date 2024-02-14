from Drawing.MATPLOTLIB import matplotlib
from Drawing.SEABORN import seaborn
from salesData import *
from FileOperation.fileOperation import *

def main():
    file_op = FileOperation()
    # Read data from the CSV file
    sales_data = file_op.read_file("../DataFiles/YafeNof.csv")
    # Create an instance of SalesData class
    sales = SalesData(sales_data)

    # ---------------------------------------------------Task 2---------------------------------------------------
    # Task 2 ex 4
    sales.eliminate_duplicates()
    # Task 2 ex 5
    total_sales_per_product = sales.caculate_total_sales()
    print("Total sales per product:", total_sales_per_product)
    # Task 2 ex 6
    total_sales_per_month = sales.caculate_total_sales_per_month()
    print("Total sales per month:", total_sales_per_month)
    # Task 2 ex 7
    best_selling_product = sales.identify_best_selling_product()
    print("Best selling product:", best_selling_product)
    # Task 2 ex 8
    month_with_highest_sales = sales.identify_month_with_highest_sales()
    print("Month with highest sales:", month_with_highest_sales)
    # Task 2 ex 9
    analysis_results = sales.analyze_sales_data()
    print("Analysis results:", analysis_results)
    # Task 2 ex 10
    analysis_results = sales.expanded_analyze_sales_data()
    print("Analysis results:", analysis_results)

    # ---------------------------------------------------Task 3---------------------------------------------------
    # Task 3 ex 11
    cumulative_sales = sales.caculate_cumulative_sales()
    print("Cumulative Sales:\n", cumulative_sales)
    # Task 3 ex 12
    sales.add_90_percent_values_column()
    # Task 3 ex 13
    sales.bar_chart_category_sum()
    # Task 3 ex 14
    mean, median, second_max = sales.caculate_mean_quantity()
    print(f'mean {mean} , median: {median} , second max: {second_max}')
    # Task 3 ex 15
    filter_by_selling_or = sales.filter_by_selling_or()
    print("Filtered products by selling or:", filter_by_selling_or)
    filter_by_selling_and = sales.filter_by_selling_and()
    print("Filtered products by selling and:", filter_by_selling_and)
    # Task 3 ex 16
    sales.divide_by_2()
    # Task 3 ex 17
    caculate_stats = sales.caculate_stats()
    print("Statistics:", caculate_stats)

    # Task 7 ex 3
    product_random = sales.random_number("Sidur")
    print(product_random)

    # ---------------------------------------------------Task 4---------------------------------------------------
    # Task 4 ex 18
    sales.convert_date_format(['Date'])
    # Task 4 ex 19
    sales.categorize_price()
    # Task 4 ex 20
    sales.change_index()
    # Task 4 ex 21
    sales.split_and_concat()
    # Task 4 ex 22
    transposed_df = sales.complex_data_transformation()
    print(transposed_df)

    # Task 4 ex 24
    index = 2
    row = sales.locate_specific_row_by_index(index)
    print("Row by index:", row)

    column_label = 'Product'
    column = sales.locate_specific_column_by_label(column_label)
    print("Column by label:", column)

    columns = ['Customer ID', 'Product', 'Price']
    start_row = 1
    end_row = 3
    result = sales.locate_specific_columns_and_range_of_rows(columns, start_row, end_row)
    print("Specific columns and range of rows:\n", result)

    start_col = 1
    end_col = 3
    rows = [0, 2, 4]
    result = sales.locate_specific_rows_and_range_of_columns(start_col, end_col, rows)
    print("Specific rows and range of columns:\n", result)

    # Task 4 ex 25
    mask_list = [True] * len(sales.data)
    filtered_df = sales.filter_by_mask(mask_list)
    print("Filtered DataFrame:")
    print(filtered_df)
    # ---------------------------------------------------Task 6---------------------------------------------------

    # ---------matplotlib---------

    matplotlib.bar_plot(total_sales_per_product.keys(), total_sales_per_product.values(),
                        "total sales per product","Products", "Total Sales")
    matplotlib.barh_plot(total_sales_per_product.keys(), total_sales_per_product.values(),
                         "total sales per product","Products", "Total Sales")
    matplotlib.pie_plot(total_sales_per_product.keys(), total_sales_per_product.values(),
                        "total sales per product")
    matplotlib.scatter_plot(total_sales_per_product.keys(), total_sales_per_product.values(),
                            "total sales per product", "Products", "Total Sales")
    matplotlib.line_plot(total_sales_per_product.keys(), total_sales_per_product.values(),
                         "total sales per product", "Products", "Total Sales")
    matplotlib.violin_plot(total_sales_per_product.values(), "Sales")
    matplotlib.fill_between_plot(total_sales_per_product.values(), 1, 1200)
    matplotlib.histogram(total_sales_per_product.values())

    # --------------seaborn----------

    seaborn.seaborn_line_plot(total_sales_per_month.keys(), total_sales_per_month.values(),
                              "Total Sales Per Month", "Month", "Total Sales")
    seaborn.seaborn_scatter_plot(total_sales_per_month.keys(), total_sales_per_month.values(),
                                 "Total Sales Per Month", "Month", "Total Sales")
    seaborn.seaborn_bar_plot(total_sales_per_month.keys(), total_sales_per_month.values(),
                             "Total Sales Per Month", "Month", "Total Sales")
    seaborn.seaborn_box_plot(total_sales_per_month.keys(), total_sales_per_month.values(),
                             "Total Sales Per Month", "Month", "Total Sales")
    seaborn.seaborn_violin_plot(total_sales_per_month.keys(), total_sales_per_month.values(),
                                "Total Sales Per Month", "Month", "Total Sales")

    # ---------------------------------------------------Task 7---------------------------------------------------

    # Task 7 ex 2
    file1 = file_op.read_file("../DataFiles/example.docx")
    file2 = file_op.read_file("../DataFiles/example.csv")
    file3 = file_op.read_file("../DataFiles/output.xlsx")
    print(file1)
    print(file2)
    print(file3)

    # Task 7 ex 4
    print("Task 7 ex 4")
    SalesData.print_python_version()

    # Task 7 ex 5
    print("Task 7 ex 5")
    param1 = 10
    param2 = 3.14
    param3 = "Hello"
    param4 = [1, 2, 3]
    result = SalesData.process_parameters(param1, param2, message=param3, data=param4)
    print("Processed parameters:", result)

    # Task 7 ex 6
    sales.print_table_star()

    # Task 7 ex 7
    sales.iterate_table_in_one_loop()


if __name__ == "__main__":
    main()
