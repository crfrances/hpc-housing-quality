#define necessary helper functions
def clean_text(text):
    """This function is used to clean a selection of text. 
    It uses several regular expressions and built in text commands in order to remove commonly seen 
    errors,
    nonsense values, 
    punctuation, 
    digits, and 
    extra whitespace.

    Args:
        text (str): This is a text value that needs to be cleaned.

    Returns:
        text: This function returns a cleaned version of the input text.
        
    TODO: Add functionality to input a selected value for NaN or missing values?

    """
    #import necessary modules
    import re
    
    #force all vals in series to string
    text = str(text)
    
    #first remove uppercase
    text = text.lower()
    
    #remove common errors
    text = re.sub(r"\[.]", "", text) 
    text = re.sub(r"\<ff>", "", text)   
    text = re.sub(r"\<fb>", "", text)
    text = re.sub(r"\<a\d>", "", text)   
    text = re.sub(r"\<c\d>", "", text)   
    text = re.sub(r"\<d\d>", "", text)
    text = re.sub(r"\<e\d>", "", text)   
    text = re.sub(r"\<f\d>", "", text)   
    text = re.sub(r"\d+\.", "", text)

    # remove the characters [\], ['] and ["]
    text = re.sub(r"\\", "", text)    
    text = re.sub(r"\'", "", text)    
    text = re.sub(r"\"", "", text)   

    # replace punctuation characters with spaces
    filters='!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    translate_dict = dict((c, " ") for c in filters)
    translate_map = str.maketrans(translate_dict)
    text = text.translate(translate_map)
    
    # remove any remaining digit codes
    text = re.sub(r"\d+", "", text)
    
    # remove any leading/trailing/duplicate whitespace
    text = re.sub(' +', ' ', text.strip())
    
    return text
                  
def apply_to_vars(var, df, fx):
    """This is a simple wrapper function that applies 
    a given function to 
    a given pandas df column.

    Args:
        var (str): This is a string indicating which column you want to apply a function to.
        df: This is an object that points to a pandas df that you want to apply a function to a column within.
        fx: This is an object that points to the function that you want to apply.

    Returns:
        NULL: This function modifies in place.
        
    TODO: Is modifying in place the right way to accomplish this task?

    """
    df[var] = df[var].apply(fx)
    
#define master function
def read_then_clean(file_path, vars_to_clean):
    """This is the master function for this module. It uses the previously defined helper and wrapper functions,
    in order to output a clean dataset for user. It reads in a selected .csv file from a given filepath,
    and applies the previously defined cleaning functions to a list of variables provided by user.

    Args:
        file_path (str): This is a string indicating which file that you want to read in.
        vars_to_clean (list): This is a list of strings that indicate which columns you want to clean.

    Returns:
        df_raw: This is a pandas df that has columsn of text values that have been cleaned using the helper function.
        
    TODO: Is it better to return an obj called df_clean to be more explicit to user?

    """
    #import necessary modules
    import pandas as pd
    
    #read in your data
    print("~begin reading")
    df_raw = pd.read_csv(file_path, low_memory=False)
    print("data read!")
    
    #cleanup
    print("~begin cleaning")
    for x in vars_to_clean:
        apply_to_vars(x, df_raw, clean_text)
    print("data clean!")
        
    #output a clean dataset
    return df_raw