# Libraries

This project uses external libraries to read-in, use, write, and plot datasets.
It uses numpy, pandas, and matplotlib to do this.

All functions and python scripts were developed using test-driven development, as 
seen by commits/merges. 

### File Descriptions:
1. data_processor.py:
    - Has functions which make use of random matrices, including creating a random matrix,
   reading in a csv data dile into a matrix, and writing a random matrix to a csv.
    - All developed through test driven development.
    - All functions have unit tests, and comments of specific usage are found in this file.
2. unit_tests.py:
   - includes unit tests for data_processor.py and plotter.
   - implemented with continuous integration. 
3. run_functional.py / functional_tests.sh:
   - runs functional tests for the functions in data_processing.py. 
   - Uses argparse specify which test to run.
   - implemented with continous integration.
4. env.yml / library_practive.yml:
   - Use github workflows to run pycodestyle, unit tests, AND functional tests.

### Usage: 
- description of usage of data_processing functions are found within docustyle comments in the file,
and examples are found in unit_test.py.
- Run unit tests as:

*cd ./tests*

*python -m unittest unit_tests.py*

- run functional tests as:

*bash functional_tests.sh*


