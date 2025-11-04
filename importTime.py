# Measure how long it takes to multiply 100,000 numbers.
import time

def calculate_product():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100001):
        product *= i
    return product

start_time = time.time()
result = calculate_product()
end_time = time.time()
print(f'It took {end_time - start_time} seconds to calculate.')
