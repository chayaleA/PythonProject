import unittest
import warnings
from salesData import SalesData
import pandas as pd
import sys
from io import StringIO

class SalesDataTets(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        data = {
            'Customer ID': [1, 2, 3, 4, 5],
            'Date': ['01.01.2023', '01.01.2023', '01.01.2023', '01.02.2023', '01.03.2023'],
            'Product': ['A', 'B', 'A', 'B', 'C'],
            'Price': [50, 100, 50, 125, 150],
            'Quantity': [2, 1, 2, 2, 1],
            'Total': [100, 200, 100, 250, 300]
        }
        self.sales_data = SalesData(pd.DataFrame(data))

    def test_eliminate_duplicates(self):
        self.sales_data.eliminate_duplicates()
        self.assertEqual(len(self.sales_data.data), 5)

    def test_caculate_total_sales(self):
        expected_result = {'A': 200, 'B': 450, 'C': 300}
        result = self.sales_data.caculate_total_sales()
        self.assertDictEqual(result, expected_result)

    def test_caculate_total_sales_per_month(self):
        expected_result = {'January': 400, 'February': 250, 'March': 300}
        result = self.sales_data.caculate_total_sales_per_month()
        self.assertDictEqual(result, expected_result)

    def test_identify_best_selling_product(self):
        expected_result = 'B'
        result = self.sales_data.identify_best_selling_product()
        self.assertEqual(result, expected_result)

    def test_identify_month_with_highest_sales(self):
        expected_result = 'January'
        result = self.sales_data.identify_month_with_highest_sales()
        self.assertEqual(result, expected_result)

    def test_analyze_sales_data(self):
        expected_result = {'best_selling_product': 'B', 'month_with_highest_sales': 'January'}
        result = self.sales_data.analyze_sales_data()
        self.assertDictEqual(result, expected_result)

    def test_expanded_analyze_sales_data(self):
        expected_result = {
            'best_selling_product': 'B',
            'month_with_highest_sales': 'January',
            'minimest_selling_product': 'A',
            'average_of_the_sales_for_all_monthes': 316.6666666666667
        }
        result = self.sales_data.expanded_analyze_sales_data()
        self.assertDictEqual(result, expected_result)

    def test_caculate_cumulative_sales(self):
        expected_result = [100, 200, 200, 450, 300]
        result = self.sales_data.caculate_cumulative_sales().tolist()
        self.assertEqual(result, expected_result)

    def test_add_90_percent_values_column(self):
        self.sales_data.add_90_percent_values_column()
        self.assertIn('Discount', self.sales_data.data.columns)

    def test_amount_of_selling_per_product(self):
        expected_result = {'A': 4, 'B': 3, 'C': 1}
        result = self.sales_data.amount_of_selling_per_product().to_dict()
        self.assertDictEqual(result, expected_result)

    def test_bar_chart_category_sum(self):
        self.sales_data.bar_chart_category_sum()

    def test_caculate_mean_quantity(self):
        expected_result = (190.0, 200.0, 250)
        result = self.sales_data.caculate_mean_quantity()
        self.assertEqual(result, expected_result)

    def test_filter_by_selling_or(self):
        expected_result = []
        result = self.sales_data.filter_by_selling_or()
        self.assertEqual(result, expected_result)

    def test_filter_by_selling_and(self):
        expected_result = []
        result = self.sales_data.filter_by_selling_and()
        self.assertEqual(result, expected_result)

    def test_divide_by_2(self):
        expected_result = [25.0, 50.0, 25.0, 62.5, 75.0]
        self.sales_data.divide_by_2()
        self.assertIn("BlackFridayPrice", self.sales_data.data.columns)
        black_friday_prices = self.sales_data.data["BlackFridayPrice"].tolist()
        self.assertEqual(black_friday_prices, expected_result)

    def test_caculate_stats(self):
        expected_result = {
            'Total': {'Maximum': 300, 'Sum': 950, 'AbsoluteValues': 950, 'CumulativeMaximum': 300},
            'CombinedStats': {'Maximum': 300, 'Sum': 950, 'AbsoluteValues': 950, 'CumulativeMaximum': 300}
        }
        result = self.sales_data.caculate_stats(columns=['Total'])
        self.assertDictEqual(result, expected_result)

    def test_convert_date_format(self):
        self.sales_data.data = pd.DataFrame(self.sales_data.data)
        self.sales_data.convert_date_format(date_columns=['Date'])
        self.assertTrue(isinstance(self.sales_data.data['Date'].iloc[0], pd.Timestamp))

    def test_categorize_price(self):
        self.sales_data.categorize_price()
        self.assertIn('Price_Category', self.sales_data.data.columns)
        expected_categories = ['Low', 'Low', 'Low', 'Low', 'Low']
        self.assertListEqual(expected_categories, list(self.sales_data.data['Price_Category']))

    def test_change_index(self):
        """
        Test the change_index method.
        """
        self.sales_data.change_index()
        expected_index = [50, 200, 150, 500, 750]
        self.assertListEqual(list(self.sales_data.data.index), expected_index)

    def test_complex_data_transformation(self):
        transposed_df = self.sales_data.complex_data_transformation()
        transposed_df2 = self.sales_data.data.T
        self.assertTrue(transposed_df.equals(transposed_df2))

    def test_locate_specific_row_by_index(self):
        index = 2
        row = self.sales_data.locate_specific_row_by_index(index)
        self.assertIsInstance(row, pd.Series)

    def test_locate_specific_column_by_label(self):
        column_label = 'Product'
        column = self.sales_data.locate_specific_column_by_label(column_label)
        self.assertIsInstance(column, pd.Series)
        # Create a Series with the expected column
        expected_column = pd.Series(data=['A', 'B', 'A', 'B', 'C'], name='Product')
        # Compare the expected column to the actual column
        pd.testing.assert_series_equal(column, expected_column)

    def test_locate_specific_columns_and_range_of_rows(self):
        columns = ['Customer ID', 'Product', 'Price']
        start_row = 1
        end_row = 3
        result = self.sales_data.locate_specific_columns_and_range_of_rows(columns, start_row, end_row)
        self.assertIsInstance(result, pd.DataFrame)

    def test_locate_specific_rows_and_range_of_columns(self):
        start_col = 1
        end_col = 3
        rows = [0, 2, 4]
        result = self.sales_data.locate_specific_rows_and_range_of_columns(start_col, end_col, rows)
        self.assertIsInstance(result, pd.DataFrame)

    def test_filter_by_mask(self):
        # Generate a mask list with all True values
        mask_list = [True] * len(self.sales_data.data)
        filtered_df = self.sales_data.filter_by_mask(mask_list)

        # Assert that the filtered DataFrame has the same shape as the original DataFrame
        self.assertEqual(filtered_df.shape, self.sales_data.data.shape)

        # Assert that the filtered DataFrame is equal to the original DataFrame
        pd.testing.assert_frame_equal(filtered_df, self.sales_data.data)

    def test_save_modified_sales_data(self):
        # Test case when data is not None
        data = {
            'Total Sales': [100, 200, 300],
            'Average Sales': [50, 100, 150]
        }
        self.sales_data.save_modified_sales_data(data)

        # Now, read the Excel file and check if it contains the correct data
        self.sales_data = pd.read_excel("../DataFiles/analyze_sales_data.xlsx")
        self.assertTrue(self.sales_data.equals(pd.DataFrame.from_dict(data, orient='index').transpose()))

    def test_random_number(self):
        product_name = "A"
        result = self.sales_data.random_number(product_name)
        self.assertIsInstance(result, dict)
        self.assertIn("product_name", result)
        self.assertEqual(result["product_name"], product_name)
        self.assertIn("random number", result)
        self.assertIsInstance(result["random number"], float)
        self.assertIn("range_between_random", result)
        self.assertIsInstance(result["range_between_random"], str)

    def test_iterate_table_in_one_loop(self):
        result = self.sales_data.iterate_table_in_one_loop()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for value in result:
            self.assertIsInstance(value, (int, float))

    def test_process_parameters(self):
        arg1 = 10
        arg2 = 20.5
        arg3 = "example"
        kwargs = {'param1': 'value1', 'param2': 100}
        result = self.sales_data.process_parameters(arg1, arg2, arg3, **kwargs)
        self.assertIsInstance(result, dict)
        self.assertIn('param1', result)
        self.assertEqual(result['param1'], kwargs['param1'])
        self.assertIn('param2', result)
        self.assertEqual(result['param2'], kwargs['param2'])

    def test_print_table(self):
        saved_stdout = sys.stdout
        sys.stdout = StringIO()
        self.sales_data.print_table_star()
        printed_output = sys.stdout.getvalue()
        sys.stdout = saved_stdout
        self.assertIn("First 3 Rows:", printed_output)
        self.assertIn("Last 2 Rows:", printed_output)
        self.assertIn("Random Row:", printed_output)

    if __name__ == '__main__':
        unittest.main()
