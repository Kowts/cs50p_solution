# Prompt the user to input a value for mass (m) and store it in the variable 'm'.
m = int(input("Enter mass: "))

# The speed of light (c) is set to a constant value of 300,000,000 meters per second.
c = 300000000

# Calculate the energy (E) using the mass-energy equivalence formula E = m * c^2,
# where 'c' is the speed of light and 'm' is the mass provided by the user.
E = m * (c ** 2)

# Print the calculated energy value.
print(E)
