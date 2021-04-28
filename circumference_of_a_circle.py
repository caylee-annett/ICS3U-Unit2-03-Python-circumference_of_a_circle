#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program calculates the circumference of a circle using tau and
#   dimensions that the user entered

import constants


def main():
    # This function calculates the circumference

    # Input
    radius_of_circle = int(input("Enter the radius of the circle (cm): "))

    # Process
    circumference = constants.TAU * radius_of_circle

    # Output
    print(
        "The circumference of a circle with radius {0} cm is: {1} cm.".format(
            radius_of_circle, circumference
        )
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
