# Function 1: ticket_price
def ticket_price(age, is_member):
    if is_member:  
        return 7
    elif not is_member and age < 12:  
        return 5
    elif not is_member and age >= 60: 
        return 6
    else:  
        return 10

# Function 2: process_transactions
def process_transactions(transactions):
    return [x**2 for x in transactions if x >= 100 or x <= -100]

# Function 3: extract_acronyms
def extract_acronyms(product_name):
    acronym = ''.join(word[0].upper() for word in product_name.split())
    return acronym

# Function 4: multiply_vectors
def multiply_vectors(row_vector, col_vector):
    if len(row_vector) != len(col_vector):
        return "The vectors must be of the same length."
    
    dot_product = 0
    for i in range(len(row_vector)):
        dot_product += row_vector[i] * col_vector[i]
    
    return dot_product

# Test cases for all functions

# Testing ticket_price function
print("ticket_price Test Cases:")
print(ticket_price(10, True))   # Member, child (should return 7)
print(ticket_price(25, False))  # Non-member, adult (should return 10)
print(ticket_price(8, False))   # Non-member, child (should return 5)
print(ticket_price(65, False))  # Non-member, senior (should return 6)

# Testing process_transactions function
print("\nprocess_transactions Test Cases:")
print(process_transactions([50, -120, 200, -80, 300]))  # Should return [14400, 40000, 90000]
print(process_transactions([150, -90, 0, 30]))  # Should return [22500]
print(process_transactions([10, 5, -60, 100]))  # Should return [10000, 10000]

# Testing extract_acronyms function
print("\nextract_acronyms Test Cases:")
print(extract_acronyms("International Business Machines"))  # Should return 'IBM'
print(extract_acronyms("Hyper Text Markup Language"))       # Should return 'HTML'
print(extract_acronyms("Portable Network Graphics"))        # Should return 'PNG'

# Testing multiply_vectors function
print("\nmultiply_vectors Test Cases:")
print(multiply_vectors([1, 2, 3], [4, 5, 6]))  # Should return 32 (1*4 + 2*5 + 3*6)
print(multiply_vectors([1, 3], [4, 5]))        # Should return 19 (1*4 + 3*5)
print(multiply_vectors([1, 2], [4, 5, 6]))    # Should return "The vectors must be of the same length."
