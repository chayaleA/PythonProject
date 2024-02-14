import random
import sys
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from FileOperation.fileOperation import *

class SalesData:
    def __init__(self, data):
        self.data = data

    # Task 2 ex 4
    def eliminate_duplicates(self):
        """
            Detects and eliminates duplicate rows in the dataset to ensure data integrity and consistency.
        """
        self.data.dropna(inplace=True)
        self.data.drop_duplicates(inplace=True)

    # Task 2 ex 5
    def caculate_total_sales(self):
        """
            Caculate the total sales for each product.

            Returns:
                - A dictionary that contains for each product it's total sales.
        """
        total_sales_per_product = self.data.groupby('Product')['Total'].sum()
        return total_sales_per_product.to_dict()

    # Task 2 ex 6
    def caculate_total_sales_per_month(self):
        """
            Caculate the total sales for each month.

            Returns:
                - A dictionary that contains for each month it's total sales.
        """
        try:
            self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')
        except ValueError:
            print(f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}> "
                  f"Error: Invalid date format in the 'Date' column. <Chaya>")
            return None
        total_sales_per_month = self.data.groupby(self.data['Date'].dt.strftime('%B'))['Total'].sum()
        return total_sales_per_month.to_dict()

    # Task 2 ex 7
    def identify_best_selling_product(self):
        """
            Identifies the best-selling product.

        Return:
            - the name of the best-selling product
        """
        total_sales_per_product = self.caculate_total_sales()
        best_selling_product = max(total_sales_per_product, key=total_sales_per_product.get)
        return best_selling_product

    # Task 2 ex 8
    def identify_month_with_highest_sales(self):
        """
            Identifies the month with the highest total sales.

            Return:
                - the month with the highest total sales.
        """
        total_sales_per_month = self.caculate_total_sales_per_month()
        month_with_highest_sales = max(total_sales_per_month, key=total_sales_per_month.get)
        return month_with_highest_sales

    # Task 2 ex 9
    def analyze_sales_data(self):
        """
            Performs the analysis using the previously defined private methods.

         Return:
            - a dictionary with the analysis results.
        """
        analysis_results = {'best_selling_product': self.identify_best_selling_product(),
                            'month_with_highest_sales': self.identify_month_with_highest_sales()}
        return analysis_results

    # Task 2 ex 10
    def expanded_analyze_sales_data(self):
        """
            Performs the analysis using the previously defined private methods.

            Return:
                - a dictionary with the analysis results.
        """
        analysis_results = self.analyze_sales_data()
        analysis_results["minimest_selling_product"] = min(self.caculate_total_sales(),
                                                           key=self.caculate_total_sales().get)
        analysis_results["average_of_the_sales_for_all_monthes"] = mean(self.caculate_total_sales_per_month().values())
        self.save_modified_sales_data(analysis_results)
        return analysis_results

    # ---------------------choice------------------
    # Task 3 ex 11
    def caculate_cumulative_sales(self):
        """
            Calculate the cumulative sum of sales for each product across months.
        """
        cumulative_sales = self.data.groupby('Product')['Total'].cumsum()
        return cumulative_sales

    # Task 3 ex 12
    def add_90_percent_values_column(self):
        """
            Create a new column ('Discunt') in the SalesData DataFrame that contains the 90% values
            of the 'Total' column.
        """
        ninety_percent_values = self.data['Total'] * 0.9
        self.data['Discount'] = ninety_percent_values

    def amount_of_selling_per_product(self):
        """
            Caculate the amount of selling per product and returns it.
        """
        return self.data.groupby('Product')['Quantity'].sum()

    # Task 3 ex 13
    def bar_chart_category_sum(self):
        """
        Plot a bar chart to represent the sum of quantities sold for each product using Seaborn.
        """
        sum_of_quantity_per_product = self.amount_of_selling_per_product().reset_index()
        sns.barplot(data=sum_of_quantity_per_product, x="Product", y="Quantity", hue="Product")
        plt.title("Sum of Quantities Sold for Each Product", fontsize=16)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Task 3 ex 14
    def caculate_mean_quantity(self):
        """
            Calculate the mean, median, and second max for Total column using NumPy array manipulation.
        """
        total_values = self.data["Total"].values
        average = np.mean(total_values)
        median = np.median(total_values)
        second_max = np.partition(total_values, -2)[-2]
        return average, median, second_max

    # Task 3 ex 15
    def filter_by_selling_or(self):
        """
            Filter specific products based on the following condition:
                - If the number of sales is more than 5 or the number of sales is equal to 0.

            Returns:
                Filtered DataFrame containing products that satisfy the condition.
        """
        amount_of_selling_per_product = self.amount_of_selling_per_product()
        filtered_products = amount_of_selling_per_product[(amount_of_selling_per_product > 5)
                                                          | (amount_of_selling_per_product == 0)].index
        return list(filtered_products)

    # Task 3 ex 15
    def filter_by_selling_and(self):
        """
            Filter specific products based on the following condition:
                - If the price is above $300 and sold less than 2 times.

            Returns:
                Filtered DataFrame containing products that satisfy the condition.
         """

        amount_of_selling_per_product = self.amount_of_selling_per_product()
        sold_less_than_2_times = amount_of_selling_per_product[amount_of_selling_per_product < 2].index
        price_above_300 = self.data[self.data["Price"] > 500]["Product"].unique()
        filtered_products = list(set(price_above_300) & set(sold_less_than_2_times))
        return filtered_products

    # Task 3 ex 16
    def divide_by_2(self):
        """
            Implement an operation to divide all values in the SalesData DataFrame by 2 for "BLACK FRIDAY".
            Column name will be "BlackFridayPrice".
        """
        self.data["BlackFridayPrice"] = self.data["Price"] / 2

    # Task 3 ex 17
    def caculate_stats(self, columns: str = None):
        """
            Find the maximum, sum, absolute values, and cumulative maximum of the SalesData DataFrame
            for all columns, and for every column separately.
        """
        if columns is None:
            columns = self.data.columns

        stats = {}
        combined_stats = {
            'Maximum': 0,
            'Sum': 0,
            'AbsoluteValues': 0,
            'CumulativeMaximum': 0
        }

        for col in columns:
            if col in ['Date', 'Product']:
                continue
            col_stats = {
                'Maximum': self.data[col].max(),
                'Sum': self.data[col].sum(),
                'AbsoluteValues': self.data[col].abs().sum(),
                'CumulativeMaximum': self.data[col].cummax().iloc[-1]
            }

            stats[col] = col_stats

            combined_stats['Maximum'] += col_stats['Maximum']
            combined_stats['Sum'] += col_stats['Sum']
            combined_stats['AbsoluteValues'] += col_stats['AbsoluteValues']
            combined_stats['CumulativeMaximum'] += col_stats['CumulativeMaximum']

        stats['CombinedStats'] = combined_stats
        return stats

    # Task 4 ex 18
    def convert_date_format(self, date_columns: list = None):
        """
            Convert the 'Date' columns in the SalesData DataFrame to datetime format.
        """

        if date_columns is None:
            return
        for col in date_columns:
            try:
                self.data[col] = pd.to_datetime(self.data[col], format="%d.%m.%Y", errors="coerce")
            except Exception as e:
                print(f"<Chaya, {datetime.date.today()}, {datetime.datetime.now().time()}> "
                      f"Error converting column '{col}': {e} <Chaya>")

    # Task 4 ex 19
    def categorize_price(self):
        """
            Create a new column in the DataFrame that categorizes price values.
        """
        self.data['Price_Category'] = pd.cut(self.data['Price'], bins=[0, 500, 1000, 10000],
                                             labels=['Low', 'Medium', 'High'], include_lowest=True)

    # Task 4 ex 20
    def change_index(self):
        """
            Change the indexing of the df to be by CustomerId*Price.
        """
        self.data.set_index(self.data['Customer ID'] * self.data['Price'], inplace=True)

    # ---------------------choice------------------
    # Task 4 ex 21
    def split_and_concat(self):
        """
        Cut the df into 2 df's, and then concatenate them along a specific axis.
        """
        half = len(self.data) // 2
        df1, df2 = self.data.iloc[:half].reset_index(drop=True), self.data.iloc[half:].reset_index(drop=True)
        self.data = pd.concat([df1, df2], axis=1)

    # ---------------------choice------------------
    # Task 4 ex 22
    def complex_data_transformation(self):
        """
            Create a new DataFrame with the transposed df.
        """
        transposed_df = self.data.T
        return transposed_df

    # Task 4 ex 24
    def locate_specific_row_by_index(self, index):
        """
            Locate a specific row from the df by index.
        """
        row = self.data.loc[index]
        row_alternative = self.data.iloc[index]
        return row

    # Task 4 ex 24
    def locate_specific_column_by_label(self, column_label):
        """
            Locate a specific column from the df by column label.
        """
        column = self.data[column_label]
        column_alternative = self.data.loc[:, column_label]
        return column

    # Task 4 ex 24
    def locate_specific_columns_and_range_of_rows(self, columns, start_row, end_row):
        """
            Locate specific columns and a range of rows from the df.
        """
        result = self.data.loc[start_row:end_row, columns]
        return result

    # Task 4 ex 24
    def locate_specific_rows_and_range_of_columns(self, start_col, end_col, rows):
        """
            Locate specific rows and a range of columns from the df.
        """
        result = self.data.iloc[rows, start_col:end_col]
        return result

    # Task 4 ex 25
    def filter_by_mask(self, mask_list, is_by_index=False):
        """
            Return the df filtered by the mask. If is_by_index=True, use the mask for the indexes.
        """
        if is_by_index:
            filtered_df = self.data[self.data.index.isin(mask_list)]
        else:
            filtered_df = self.data[mask_list]
        return filtered_df

    # Task 5 ex 27
    def save_modified_sales_data(self, data):
        """
            Saves modified sales data to an Excel file.
            Parameters:
                - data: A dictionary containing the modified sales data.
        """
        if data:
            df = pd.DataFrame.from_dict(data, orient='index').transpose()
            file_op = FileOperation()
            file_op.save_to_excel(df, "../DataFiles/analyze_sales_data.xlsx")
        else:
            print("Error: No data to save.")

    # Task 7 ex 3
    def random_number(self, product_name: str) -> dict:
        """
            Generates a random number for a given product.
            Parameters:
                - product_name: The name of the product for which a random number is generated.
            Returns:
                - A dictionary containing details about the random number generation process.
        """
        SalesData.print_python_version()
        numbers_of_sales = self.caculate_total_sales()[product_name]
        max_price_product = self.data.loc[self.data['Product'] == product_name, 'Price'].max()

        random_number = random.uniform(numbers_of_sales, max_price_product)

        random_details = {
            "product_name": product_name,
            "random number": random_number,
            "range_between_random": f"{numbers_of_sales} - {max_price_product}"
        }
        return random_details

    # Task 7 ex 4
    @staticmethod
    def print_python_version():
        """
            Prints the version of Python.
        """
        print(sys.version)

    # Task 7 ex 5
    @staticmethod
    def process_parameters(*args, **kwargs) -> dict:
        """
            This function iterates over the positional arguments (*args) and checks if each argument is a numerical
            value (integer or float). If it is, the function prints the numerical value. Then, it collects all keyword
            arguments (**kwargs) into a dictionary and returns the dictionary containing all the keyword arguments.

            Parameters:
                - *args: positional arguments, can be of any type
                - **kwargs: keyword arguments, can be of any type

            Returns:
                - a dictionary containing all keyword arguments provided
        """
        result = {}
        for arg in args:
            if isinstance(arg, (int, float)):
                print(arg)
        for key, value in kwargs.items():
            result[key] = value
        return result

    # Task 7 ex 6
    def print_table_star(self):
        """
           Print the first 3 rows, last 2 rows, and a random row from the DataFrame.
        """
        print("First 3 Rows:")
        for index, row in self.data.head(3).iterrows():
            print(f"Index: {index}\nData:")
            for column, value in row.items():
                print(f"{column}: {value}")
            print()
        print("Last 2 Rows:")
        for index, row in self.data.tail(2).iterrows():
            print(f"Index: {index}\nData:")
            for column, value in row.items():
                print(f"{column}: {value}")
            print()
        print("Random Row:")
        random_row_index = random.randint(0, len(self.data) - 1)
        random_row = self.data.iloc[random_row_index]
        print(f"Index: {random_row_index}\nData:")
        for column, value in random_row.items():
            print(f"{column}: {value}")

    # Task 7 ex 7
    def iterate_table_in_one_loop(self):
        """
            Iterates over the numerical values in the table using a single loop.
            Returns:
                - A list containing all the numerical values in the table.
        """
        numerical_values = []
        for col_index in range(len(self.data.columns)):
            column = self.data.iloc[:, col_index]
            if column.dtype in ['int64', 'float64']:
                numerical_values.extend(column)
                print(column)
        return numerical_values
