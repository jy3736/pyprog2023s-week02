# Time Difference Between Two Timestamps

## Objective
Write a Python program that takes two timestamps as input and returns the time difference between them in seconds.

## Requirements
The program should meet the following requirements:
- The program should define a function named `main` that takes no arguments.
- The program should accept two timestamps in the format `'hours minutes seconds'` using the input() function.
- If the second timestamp is before the first timestamp, the function should return -1.
- Otherwise, the function should return the time difference between the two timestamps in seconds.
- The program should print the output of the `main` function.

## Example usage

```
lab03> python .\main.py
10 10 10
10 12 10
120
lab03> python .\main.py
12 0 20
12 1 20
60
lab03> python .\main.py
20 0 0
19 0 0
-1
```

## Self-testing locally
It's recommended that you self-test your solution before submitting it. You can do this by running the following command in the terminal:

```
python testing.py
```

This script runs the automated tests to verify if your solution is correct or not.

Alternatively, you can run the following command if you have the "make" tool installed:

```
make
```
