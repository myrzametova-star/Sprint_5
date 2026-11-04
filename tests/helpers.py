import random

def generate_email():
    first_name = "anastasia"
    last_name = "fadeeva"
    cohort_number = "54" 
    random_digits = random.randint(100, 999)
    return f"{first_name}_{last_name}_{cohort_number}_{random_digits}@yandex.ru"