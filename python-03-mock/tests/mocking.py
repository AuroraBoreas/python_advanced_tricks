# import sys
# sys.path.append(r"D:\pj_02_pg\python-03-mock")
# from myfunc import check_dir_exists, check_file_exists, create_file, delete_file, os
from myfunc import *
import unittest
from unittest import mock

@mock.patch("builtins.open", mock=mock.mock_open)
@mock.patch("myfunc.check_dir_exists")
@mock.patch("myfunc.check_file_exists")
class MyfuncTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp: Initialize instance variable\n")
        self.directory = r"D:\pj_02_pg\python-03-mock\tests"
        self.file_name = "dummy_file_name.txt"
        self.full_path = os.path.join(self.directory, self.file_name)
    def tearDown(self):
        self.directory = ""
        self.file_name = ""
    def test_create_file_success(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print("test_create_file_success\n")
        mock_check_dir_exists.return_value = True
        mock_check_file_exists.return_value = False
        self.assertTrue(create_file(self.directory, self.file_name))
    def test_create_file_failure_dir_no_exists(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print("test_create_file_failure_dir_no_exists\n")
        mock_check_dir_exists.return_value = False
        mock_check_file_exists.return_value = False
        self.assertFalse(create_file(self.directory, self.file_name))
    def test_create_file_failure_file_already_exists(self, mock_check_dir_exists, mock_check_file_exists, mock_open_func):
        print("test_create_file_failure_file_already_exists\n")
        mock_check_dir_exists.return_value = False
        mock_check_file_exists.return_value = False
        self.assertFalse(create_file(self.directory, self.file_name))

    # @mock.patch("myfunc.os.path.isfile")
    # @mock.patch("myfunc.os.remove")
    # def test_delete_file_success(self, mock_os_path_isfile, mock_os_remove):
    #     print("test_delete_file_success")
    #     mock_os_path_isfile.return_value = True
    #     delete_file(self.full_path)
    #     mock_os_remove.assert_called_with(self.full_path)

if __name__ == "__main__":
    unittest.main()