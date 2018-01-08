import unittest
from parser import Parser


class TestSplitColumns(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parse_csv_files(self):
        filenames = ['1.csv', '2.csv', '3.csv']
        expected_output = '''1.csv
[{'day': 'mon', 'description': 'first_desc 1', 'square': 1, 'value': 1},
 {'day': 'tue', 'description': 'first_desc 25', 'square': 25, 'value': 5},
 {'day': 'wed', 'description': 'first_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'first_desc 6', 'double': 6, 'value': 3},
 {'day': 'fri', 'description': 'first_desc 6', 'double': 6, 'value': 3}]

2.csv
[{'day': 'mon', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'tue', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'wed', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'second_desc 4', 'double': 4, 'value': 2},
 {'day': 'fri', 'description': 'second_desc 6', 'double': 6, 'value': 3}]

3.csv
[{'day': 'mon', 'description': 'third_desc 9', 'square': 9, 'value': 3},
 {'day': 'tue', 'description': 'third_desc 9', 'square': 9, 'value': 3},
 {'day': 'wed', 'description': 'third_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'third_desc 4', 'double': 4, 'value': 2},
 {'day': 'fri', 'description': 'third_desc 2', 'double': 2, 'value': 1}]

'''
        output = self.parser.parse_csv_files(filenames)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
