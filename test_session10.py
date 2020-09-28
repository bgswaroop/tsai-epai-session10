import inspect
import os
import re

import session10
from session10 import *


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add at least 200 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_data_analysis_using_tuples():
    """
    Testing the method data_analysis_using_tuples
    :return: None
    """
    data_analysis_using_tuples()
    assert True


def test_data_analysis_using_dict():
    """
    Testing the method data_analysis_using_tuples
    :return: None
    """
    data_analysis_using_dict()
    assert True


def test_imaginary_stock_exchange():
    """
    Testing the method data_analysis_using_tuples
    :return: None
    """
    imaginary_stock_exchange()
    assert True
