# README

## Making a Ceasar Cipher to encrypt, decrypt, and crack ciphers! by Audrena Vacirca, Feb.7.2021

## Challenge

Create an encrypt function that takes in a plain text phrase and a numeric shift.
the phrase will then be shifted that many letters.
E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’
shifts that exceed 26 should wrap around
E.g. encrypt(‘abc’,27) would return ‘bcd’
shifts that push a letter out or range should wrap around
E.g. encrypt(‘zzz’,1) would return ‘aaa’
Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
Devise a method for the computer to determine if code was broken with minimal human guidance.

Approach & Efficiency
BigO: Time:O(1) Time is constant, not effected Space:O(n) Linear, only so many tests we can write

## Solution

Friendly reminder to always look through the given tests for key phrases, def, and names!

## Contributions:

[Ben Hill](https://github.com/ben-hill33)

[Amber Falbo](https://github.com/AmberFalbo)

[Mason Chance](https://github.com/MasonChance)
