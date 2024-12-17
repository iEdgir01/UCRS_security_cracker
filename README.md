# UCRS_security_cracker
provides dice inversion and captcha sequence for the security module in Uncle Chops Rocket Shop.

## Installation Instructions

1. **Clone the repository:**
   git clone https://github.com/iEdgir01/UCRS_security_cracker.git
2. **Ensure you have Python installed: This script is written in Python.**
    You can download it from python.org.

## Usage

1. **Run the script**
    ```bash
    python security_crack.py
    ```
2. **The script will prompt you to enter a dice number between 1 and 6.** 
    It will then return the inverse of the provided dice number based on the predefined mapping.
3. **The script will then ask for icon Attributes**
    Enter each icon's attributes in one line using the format ``(EYES)(HEAD DIRECTION)(LEGS)``:

    - EYES: Number of eyes (1-9)

    - HEAD DIRECTION: Head direction, can be one of the following:
         ```
          L for Left
          M for Middle
          R for Right
         ```

   -  LEGS: Number of legs (1-9)

    Input all three icons, pressing Enter after each. If you make a mistake, the script will prompt you to enter the icon again.

    Once all three icons are entered, the script will sort them based on the following rules:

    Number of eyes (low to high)

    Head direction (L < M < R)

    Number of legs (low to high)

## Example

![GPiNEUdWEAADmIN](https://github.com/user-attachments/assets/34a3d1f9-5521-4ea0-aca2-bbbb54079c6c)

**Identifying the Icons**
```
Icon 1(Top): 2 eyes, Middle Head, 3 Legs => 2M3
Icon 2(middle): 1 eye, Right Head, 2 Legs => 1R2
Icon 3(Bottom): 2 eyes, Left Head, 4 Legs => 2L4
```
Running the script you get: 
```
Enter a dice number (1-6), and I'll provide its inverse:
Enter dice number: 6
The inverse of 6 is 1


Enter each icon's attributes in one line using the format '(#EYES)(HEAD DIRECTION - L/M/R)(#LEGS)' (e.g., '1L4' or '2M3').
Type all three icons, pressing Enter after each. Then press Enter on an empty line to finish.
Icon 1: 2M3
Icon 2: 1R2
Icon 3: 2L4

The correct sequence is: 2, 3, 1
```
## Notes
to exit the script at any time, press ``CTRL+C``

## License
This project is licensed under the MIT License. See the LICENSE file for details.



