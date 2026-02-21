
# returns the quotient and remainder of a mod b
def proper_mod(a, b):
    quotient, remainder = divmod(a, b)
    if remainder < 0:
        remainder + b
    return quotient, remainder

#def basic_euclidean(a, b):


#def extended_euclidean(a, b):

print(proper_mod(4732987482378, -5))
