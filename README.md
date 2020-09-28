# EPAi session10 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session10 objectives
This assignment, helps to code the concepts that are learnt in the session 10 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

- Tuples as a Data Structure
- Named Tuple
- Named Tuple - Modifying & Extending
- Named Tuple - DocString & Default Values
 
---

The test cases can be executed by executing _pytest_, from python shell
 
---

### Functions


**data_analysis_using_tuples()**

    Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type,
    mean-current_location, oldest_person_age and average age (add proper doc-strings)
     : return :  None

**data_analysis_using_dict()**

    Do the same thing above using a dictionary. Prove that namedtuple is faster
     : return :  None

**imaginary_stock_exchange()**

    Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies
    (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value
    stock market started at, what was the highest value during the day and where did it end. Make sure your
    open, high, close are not totally random. You can only use namedtuple.
     : return :  None

---

### Unit Tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_data_analysis_using_tuples()**

    Testing the method data_analysis_using_tuples
     : return :  None

**test_data_analysis_using_dict()**

    Testing the method data_analysis_using_tuples
     : return :  None

**test_imaginary_stock_exchange()**

    Testing the method data_analysis_using_tuples
     : return :  None

---

#### 