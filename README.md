# Entropy Calculator
 A password entropy calculator, written in Python
 
 This script will assess the strength of a given password by calculating its entropy.

## What is password entropy?
Password entropy is a way to measure a password's strength. Entropy measures how long it will take a computer to brute-force your password. The higher the entropy, the longer it will take. This can be affected by password length and types of characters used. A higher length and more types of characters will give a better result. For example, if a password only uses lower-case letters, there are only 26 possible characters used. This will make the entropy low. In comparison, a password that uses lower-case, upper-case, digits, and special characters (#, $, ^, etc.) will have a much higher entropy because it uses more possible characters. A longer password will also have more entropy.

## How is this calculated?
Entropy is calculated using this formula:
> log<sub>2</sub>(C)*L

in which `C` is the amount of possible characters and `L` is the length of the password.

## What is a good entropy value?
Anything around 50 or above is an OK password. However, this isn't a full judgment of a password's strength, and also isn't always entirely accurate. See the disclaimer for more details.

## Disclaimer
This script does not take wordlists or dictionary attacks into account, so the output of this does not fully determine password security.
