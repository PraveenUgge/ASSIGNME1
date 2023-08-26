# Opening Comment
"""
    Title: Fermat's Last Theorem Near Misses
    File: fermat_near_misses.py
    External Files: None
    Created by: Praveen Ugge
    Course Number: SU23-CPSC-60500-002
    Date: 26/8/2023
    Description: This program searches for near misses of Fermat's Last Theorem using user input for n and k.
    Resources Used: [List any external resources used, if applicable]
"""

import sys

# Function to calculate the relative miss
def relative_miss(x, y, z, n):
    miss_zn = abs(x**n + y**n - z**n)
    miss_zn1 = abs(x**n + y**n - (z+1)**n)
    return min(miss_zn, miss_zn1) / (x**n + y**n)

def main():


    print("Software Engineering: Assignment 1 - Fermat's Last Theorem Near Misses")

    # Get user input for n and k
    n = int(input("Enter the value of n (2 < n < 12): "))
    k = int(input("Enter the value of k (k >= 10): "))

    # Check input constraints
    if n <= 2 or n >= 12 or k < 10:
        print("Invalid input. Please follow the input constraints.")
        sys.exit(1)

    min_relative_miss = float('inf')

    # Loop through possible combinations of x, y, and z
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            for z in range(1, x + y + 1):  # z is not directly constrained
                rel_miss = relative_miss(x, y, z, n)
                if rel_miss < min_relative_miss:
                    min_relative_miss = rel_miss
                    best_x, best_y, best_z = x, y, z

    # Print the best near miss
    print("\nBest Near Miss:")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}")
    print(f"Actual Miss = {int((best_x**n + best_y**n) - best_z**n)}")
    print(f"Relative Miss = {min_relative_miss * 100:.2f}%")

if __name__ == "__main__":
    main()
