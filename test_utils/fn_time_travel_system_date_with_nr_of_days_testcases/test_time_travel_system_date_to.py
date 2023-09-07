import filecmp, os, sys
sys.path.append('c:\\dev\\pytWinc\\superpy')
sys.path.append('c:\\dev\\pytWinc\\superpy\\utils_superpy')
from utils_superpy.utils import get_path_to_directory_of_file, time_travel_system_date_with_nr_of_days

directory_of_testcase = "fn_time_travel_system_date_with_nr_of_days_testcases" 
path_to_directory_of_testcase = get_path_to_directory_of_file(directory_of_testcase)

# input test files:
path_to_input_file_test_01 = os.path.join(path_to_directory_of_testcase, "test_input", 'input_file_for_test01.txt') 
path_to_input_file_test_02 = os.path.join(path_to_directory_of_testcase, "test_input", 'input_file_for_test02.txt') 
path_to_input_file_test_03 = os.path.join(path_to_directory_of_testcase, "test_input", 'input_file_for_test03.txt') 

# actual results:
path_to_actual_testresults_directory = os.path.join(path_to_directory_of_testcase, 'actual_testresults') 
path_to_file_with_actual_result_test_01 = os.path.join(path_to_actual_testresults_directory, 'actual_result_test_01.txt') 
path_to_file_with_actual_result_test_02 = os.path.join(path_to_actual_testresults_directory, 'actual_result_test_02.txt') 
path_to_file_with_actual_result_test_03 = os.path.join(path_to_actual_testresults_directory, 'actual_result_test_03.txt') 


# expected results:
path_to_file_with_expected_result_01 = os.path.join(path_to_directory_of_testcase, "expected_testresults",  'expected_result_test_01.txt') 
path_to_file_with_expected_result_02 = os.path.join(path_to_directory_of_testcase, "expected_testresults", 'expected_result_test_02.txt') 
path_to_file_with_expected_result_03 = os.path.join(path_to_directory_of_testcase, "expected_testresults", 'expected_result_test_03.txt') 


def test_01_time_travel_to_the_future():
    filecmp.clear_cache()
    time_travel_system_date_with_nr_of_days(5, path_to_input_file_test_01, path_to_file_with_actual_result_test_01)
    assert filecmp.cmp(path_to_file_with_actual_result_test_01, path_to_file_with_expected_result_01, shallow=False)

def test_02_time_travel_to_the_future_actual_result_not_same_as_expected_result():
    filecmp.clear_cache()
    time_travel_system_date_with_nr_of_days(4, path_to_input_file_test_02, path_to_file_with_actual_result_test_02)
    assert not filecmp.cmp(path_to_file_with_actual_result_test_02, path_to_file_with_expected_result_02, shallow=False)


def test_03_time_travel_to_the_future_actual_result_not_same_as_expected_result():
    filecmp.clear_cache()
    time_travel_system_date_with_nr_of_days(7, path_to_input_file_test_03, path_to_file_with_actual_result_test_03)
    assert filecmp.cmp(path_to_file_with_actual_result_test_03, path_to_file_with_expected_result_03, shallow=False)