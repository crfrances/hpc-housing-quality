#write tests
"""This is a module used to test a module: "prep.py" and its relevant functions read_then_clean and clean_text

read_then_clean is a function that takes a csv with messy string values and 
creates then cleans a pandas df
using clean_text

This module tests that function by ensuring that it returns expected exceptions and
does not contain unexpected values.
"""
# import packages
import pytest
import pandas as pd
import re

#import custom modules fpr testing
import sys 
sys.path.append('.')
import prep.prep_data as prep

#set globals for tests
FILEPATH = '../data/example_data.csv'
CLEAN_COLS = ['housing_roof', 'housing_wall', 'housing_floor']
DIGITS = str([str(x) for x in range(100 + 1)])
PUNCT = '!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
SPACE = '     '

# if you compile the regex string first, it's even faster
re_dig = re.compile('\d')
re_punct = re.compile('\W+')
re_white = re.compile(' +')

def test_globals():
    """This function tests that the test globals are properly defined.
    """
    #assert that digits are removed
    assert re_dig.search(DIGITS) != None, "global doesn't contain digits!" 
    #assert that punctutation is removed
    assert re_punct.search(PUNCT) != None, "global doesn't contain punctuation!"
    #assert that excessive whitespace is removed
    assert re_white.search(SPACE) != None, "global doesn't contain whitespace!"
    

def test_clean_text():
    """This function tests that the clean text function is doing its job.
    """
    #assert that digits are removed
    assert re_dig.search(prep.clean_text(DIGITS)) == None, "clean_text did not remove the digits from test global." 
    #assert that punctutation is removed
    assert re_punct.search(prep.clean_text(PUNCT)) == None, "clean_text did not remove the punctuation from test global."
    #assert that excessive whitespace is removed
    assert re_white.search(prep.clean_text(SPACE)) == None, "clean_text did not remove the whitespace from test global."

# This is our base dataset and it needs to be cleaned properly. The second argument specifies
# the cols with string values that we want to be cleaned.


#TODO, how to cause read_then_clean to raise the row count exception??
def test_read_then_clean():
    """This function tests that a custom exception called RowCountException
    will be returned when more than 1k rows are expected.
    """
    #read in df using your function and then using pandas regular csv read, then compare the resulting dfs
    test_df = prep.read_then_clean(FILEPATH, CLEAN_COLS)
    test_raw = pd.read_csv(FILEPATH)
    
    #assert that our function did not add or remove rows
    assert len(test_csv) == len(df), "read_then_clean function is modifying the original csv's length"
    assert len(df.columns) == len(test_csv.columns), "read_then_clean function is modifying the original csv's width"
    
    #assert that our function cleaned up the strings in the columns we provided
    #TODO, this test will fail if the columns were entirely clean to begin with (is this possible?)
    for x in CLEAN_COLS:
        assert set(df[x].unique()) == set(test_csv[x].unique()) == False, "string columns are unmodified"
