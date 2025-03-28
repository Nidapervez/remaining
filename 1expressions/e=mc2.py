"""
Program: mass_energy_calculator
-------------------------------
Calculates energy from mass using Einstein's mass-energy equivalence formula:
E = m * C^2
"""

# Define the speed of light constant (in meters per second)
C = 299792458  

def main():
    """
    Reads mass input from the user and calculates the equivalent energy using E = m * C^2.
    """
    # Get mass input from the user
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's equation
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display results
    print("\ne = m * C^2...\n")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"\n{energy_in_joules} joules of energy!")

# Required line to execute main() when running the script
if __name__ == '__main__':
    main()
