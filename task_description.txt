Write a parser that will print to the console result of parsing of 3 provided CSV files.

In the csv files you can find a data for 5 days of a week: mon, tue, wed, thu, fri. Days may be provided in range format: `mon-thu`.
For each day you should store a value, description and some day's specific data:
1. For mon, tue and wed it is a `square` field.
2. For thu, fri it is a `double` field.

In csv there is also some additional data which should be skipped.

Please note that `description` field contains day's specific data.

Expected output:
1.csv
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


Please provide solution for above problem.
Your code should:
- Include tests.
- Include a README.md file in the root describing how to run the app, how to
run tests and any dependencies needed from the system
- Work on Python 2.7 or Python 3.x 

You may use a dependency management system and as many dependencies as you like.
Please provide a link to a public VCS (github, etc)
