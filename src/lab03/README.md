# Hello World

## Objective
Write a Python program that takes two timestamps as input and returns the time difference between them in seconds.

## Requirements
The program should meet the following requirements:
- The program should define a function named `main` that takes no arguments.
- The function should prompt the user to input two timestamps in the format "hours minutes seconds".
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

## Self-Testing with make
It's recommended that you self-test your solution before submitting it. You can do this by running the following command in the terminal:

```
python testing.py
```

This script runs the automated tests to verify if your solution is correct or not.

Alternatively, you can run the following command if you have the "make" tool installed:

```
make
```

This will also run the automated tests to verify if your solution is correct or not. If you don't have the "make" tool installed, you can use the first command to test your solution.