import csv


def search(first_name=None, last_name=None, address=None, tax_id=None):
    # helper function to transform the keys
    def transform(obj):
        new_dict = {}
        for key, val in obj.items():
            new_key = '_'.join(key.lower().split())
            new_dict[new_key] = val
        return new_dict

    file = "people.csv"  # names file
    people = []

    with open(file, 'r') as data:  # open file and names it data
        # loops through the file and used csv library to iterate from list to dictionary
        csv_reader = csv.DictReader(data)
        for item in csv_reader:
            transformed_item = transform(item)
            people.append(transformed_item)

    # if no arguments provided, return the entire list
    if first_name is None and last_name is None and address is None and tax_id is None:
        return people

    # searches = {'first_name,last_name,address,tax_id'}
    if first_name and last_name and tax_id:
        return list(filter(lambda x: x['first_name'].lower() == first_name.lower()
                           and x['last_name'].lower() == last_name.lower()
                           and x['tax_id'].lower() == tax_id.lower(), people))

    # searches = {'first_name,last_name'}
    elif first_name and last_name:
        return list(filter(lambda x: x['first_name'].lower() == first_name.lower()
                           and x['last_name'].lower() == last_name.lower(), people))

    # searches = {'last_name'}
    elif last_name is not None:
        return list(filter(lambda x: x['last_name'].lower() == last_name.lower(), people))

    # searches = {'last_name'}
    elif first_name is not None:
        return list(filter(lambda x: x['first_name'].lower() == first_name.lower(), people))

    elif tax_id and not (first_name and last_name):
        return list(filter(lambda x: x['tax_id'].lower() == tax_id.lower(), people))

    elif address is not None:
        return list(filter(lambda x: x['address'].lower() == address.lower(), people))

    return None


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
assert (search(first_name='manny', last_name='macho') == result)
assert (search(first_name='MANNY', last_name='MACHO') == result)

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
assert (search(last_name='LinColN') == result)
#
assert (search(tax_id='924620110')[0]['last_name'] == 'Fox')
#
# # An empty list should be returned if the search criteria doesn't match
# # any records
assert (search(address='1986 Diagon Alley') == [])
assert (search(first_name='Richard', last_name='Fox', tax_id='0') == [])
#
# # Test if the search function is accidentally considering the header
# # row to be a valid person record
assert (search(first_name="First Name") == [])
#
# # Passing no criteria should result in the search returning the entire
# # list of people
assert (len(search()) == 9)
