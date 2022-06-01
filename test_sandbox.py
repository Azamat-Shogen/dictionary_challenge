import csv

def search(first_name=None, last_name=None, address=None, tax_id=None):
    #searches = {'first_name,last_name,address,tax_id'}
    
    file = "dictionaries/people.csv" #names file
    
    with open(file) as data: #open file and names it data
      
        for people in csv.DictReader(data): #loops thru the file and used csv library to iteriate from lis tto dictionary 

pass
            
    
    
    

        
         
    
    
    # Implement this function

########################################################
# Assertion tests to ensure "search" behaves correctly #
########################################################
result = [
    {
        'first_name': 'Manny',
        'last_name': 'Macho',
        'address': '123 Harvard Ave, Somerville, MA, 02114',
        'tax_id': '387123897'
    }
]
assert(search(first_name='manny', last_name='macho') == result)
assert(search(first_name='MANNY', last_name='MACHO') == result)

result = [
    {
        'first_name': 'Boris',
        'last_name': 'Lincoln',
        'address': '111 Haskell Hall, Medford, MA 02155',
        'tax_id': '321659876'
    },
    {
        'first_name': 'Donna',
        'last_name': 'Lincoln',
        'address': '111 Haskell Hall, Medford, MA 02155',
        'tax_id': '334561468'
    }    
]
assert(search(last_name='LinColN') == result)

assert(search(tax_id='924620110')[0]['last_name'] == 'Fox')

# An empty list should be returned if the search criteria doesn't match
# any records
assert(search(address='1986 Diagon Alley') == [])
assert(search(first_name='Richard', last_name='Fox', tax_id='0') == [])

# Test if the search function is accidentally considering the header
# row to be a valid person record
assert(search(first_name="First Name") == [])

# Passing no criteria should result in the search returning the entire
# list of people
assert(len(search()) == 9)
