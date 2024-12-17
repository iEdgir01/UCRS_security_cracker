# UCRS_security_cracker
provides dice inversion and captcha sequence for the security cracker in Uncle Chops Rocket Shop.

## Installation Instructions

1. **Clone the repository:**
   git clone https://github.com/iEdgir01/UCRS_security_cracker.git
2. **Ensure you have Python installed: This script is written in Python.**
    You can download it from python.org.

## Usage

1. **Run the script**
    python security_crack.py
2. **The script will prompt you to enter a dice number between 1 and 6.** 
    It will then return the inverse of the provided dice number based on the predefined mapping.
3. **The script will then ask for icon Attributes**
    Enter each icon's attributes in one line using the format (EYES)(HEAD DIRECTION)(LEGS):

    EYES: Number of eyes (1-9)

    HEAD DIRECTION: Head direction, can be one of the following:

    L for Left
    M for Middle
    R for Right

    LEGS: Number of legs (1-9)

    Input all three icons, pressing Enter after each. If you make a mistake, the script will prompt you to enter the icon again.

    Once all three icons are entered, the script will sort them based on the following rules:

    Number of eyes (low to high)

    Head direction (L < M < R)

    Number of legs (low to high)

## Example
