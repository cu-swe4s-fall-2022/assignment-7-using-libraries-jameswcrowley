. ssshtest

run test_random_matrix_size python run_functional.py --test_type='random_matrix'
assert_in_stdout 3
assert_exit_code 0

run test_read_in python run_functional.py --test_type='read_in'
assert_in_stdout 3
assert_exit_code 0