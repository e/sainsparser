#!/usr/bin/python

from __future__ import print_function
from collections import OrderedDict
import json
import re


DAYS = ['mon', 'tue', 'wed', 'thu', 'fri']


class Parser:
    def build_day_data(self, day, description, value):
        data_type = 'square'
        computed_value = str(int(value) ** 2)
        if day in ['thu', 'fri']:
            data_type = 'double'
            computed_value = str(int(value) * 2)
        numdesc = ' '.join([description, computed_value])
        day_data = OrderedDict()
        day_data['day'] = day
        day_data['description'] = numdesc
        day_data[data_type] = int(computed_value)
        day_data['value'] = int(value)
        return day_data

    def build_output_from_csv_data(self, filename, data_days):
        output = filename + '\n['
        output += ',\n '.join([re.sub(
            '"', "'", json.dumps(item)) for item in data_days])
        output += ']'
        return output

    def split_columns(self, lines):
        if len(lines) != 2:
            raise Exception('Incorrect input. More than 2 lines.')
        columns = lines[0].split(',')
        data = lines[1].split(',')
        if len(columns) != len(data):
            message = ('Incorrect input. Number of columns does not match \
                       length of data.')
            raise Exception(message)
        return [columns, data]

    def parse_data(self, lines):
        data = {}
        data_keys = set(DAYS + ['description'])
        for i in range(len(lines[0])):
            if lines[0][i] in data_keys:
                data[lines[0][i]] = lines[1][i]
            elif '-' in lines[0][i]:
                days = lines[0][i].split('-')
                if all(day in DAYS for day in days):
                    for j in range(DAYS.index(days[0]),
                                   DAYS.index(days[1]) + 1):
                        data[DAYS[j]] = lines[1][i]
        if set(data.keys()) != data_keys:
            print(data)
            print(data_keys)
            message = ('Incorrect input. Please check the data.')
            raise Exception(message)
        return data

    def read_csv(self, filename):
        lines = []
        with open(filename, 'r') as f:
            lines.append(f.readline().rstrip())
            lines.append(f.readline().rstrip())
        return lines

    def parse_csv_files(self, filenames):
        output = ''
        for filename in filenames:
            lines = self.read_csv(filename)
            data_orig = self.split_columns(lines)
            parsed_data = self.parse_data(data_orig)
            description = parsed_data.get('description')
            output_data = []
            for day in DAYS:
                value = parsed_data.get(day)
                day_data = self.build_day_data(day, description, value)
                output_data.append(day_data)
            output += self.build_output_from_csv_data(filename, output_data)
            output += '\n\n'
        return output


if __name__ == '__main__':
    import argparse
    argparser = argparse.ArgumentParser(description='Parse CSV files')
    argparser.add_argument('filenames', type=str, nargs='+', help='Filenames')
    args = argparser.parse_args()
    parser = Parser()
    print(parser.parse_csv_files(args.filenames))
