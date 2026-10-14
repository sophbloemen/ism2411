#---Excercise 1: Functions---

def calculate_tax(price, rate):
    tax = price * rate
    return tax

#Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")

#---Excercise 2: Functions ---

# Defining a function
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#---Excercise 3: Functions ---
def final_price(price, tax_rate, discount_tier):
    tax = calculate_tax(price, tax_rate)
    discounted_price = apply_discount(price, discount_tier)
    return discounted_price + tax
#calling final price
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#---Excercise 4: Functions ---

orders = [(200, 'gold'), (150, 'silver'), (100, 'bronze'), (500, 'none')]

rate = 0.07

for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Order: ${price}, Tier: {tier}, Final Price: ${total:.2f}")

#--Exercise 6 Functions ---

x = 100            # global x
def double_it():
    x = 999
    return x * 2     # local x
print(x)
print(double_it())
print(x)

# --- SELF-ASSESSMENT QUESTIONS ---

# --- SELF-ASSESSMENT QUESTIONS ---

# Question 1: 
# A TypeError in broken_sales.py from the terminal traceback line number
# Using the Python traceback first shows debugging instincts by fixing blocks before tracing logic

# Question 2: 
# Takes an items original price and customer loyalty, then gives the final discounted price 
# Inputs: price and tier
# Return: discounted price
# Yes a colleague can look at the function name, inputs, and return type without reading the body logic

# Question 3:
# Used AI to explain Python traceback errors in Exercise 5 no AI was used in Exercises 1-4 or 6
# Using AI to translate error messages helped me look for what to spot when looking for errors