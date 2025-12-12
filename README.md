Temperature Converter — Python

A simple, clean, menu-based temperature converter that supports conversions between Celsius (C), Fahrenheit (F), and Kelvin (K).

This CLI tool includes a main converter, quick conversion mode, and example conversions for easy reference.

Features
1. Convert any temperature

Supports full range of conversions:

C → F

F → C

C → K

K → C

F → K

K → F

2. Quick Conversion Mode

Fast conversions without selecting units again:

a) C → F

b) F → C

c) C → K

d) K → C

3. Example Conversions

Shows common temperature conversion results to help understand formulas.

4. Full Input Validation

Ensures only valid temperature values and units are accepted.

Installation & Usage
1. Clone the repository
git clone <your-repository-url>

2. Open the project folder
cd Temperature-Converter

3. Run the program
python main.py


(Or whatever filename you used.)

Example Output
-------------------------------------
Temperature Converter - C <-> F <-> K
-------------------------------------

1) Convert temperature
2) Show example conversions
3) Quick conversions (fixed: C→F, F→C, C→K, K→C)
4) Exit
Select (1-4):

Conversion Formulas Used
Celsius → Fahrenheit

°F = (°C × 9/5) + 32

Fahrenheit → Celsius

°C = (°F − 32) × 5/9

Celsius → Kelvin

K = °C + 273.15

Kelvin → Celsius

°C = K − 273.15

Fahrenheit → Kelvin

Convert F → C → K

Kelvin → Fahrenheit

Convert K → C → F

Example Conversions (Built-in)

0°C = 32°F

32°F = 0°C

100°C = 373.15K

300K ≈ 80.33°F

Tech Stack

Python 3

Standard Input/Output CLI

No external libraries required

Author

Aryan Sonsurkar
Python Developer • Student • Creator

This is a beginner-friendly but well-structured project showcasing clean logic and CLI handling.

Show Support

If you like this project, don’t forget to:

Star the repository

Share it

Improve it with your own ideas