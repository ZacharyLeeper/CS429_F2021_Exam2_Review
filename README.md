# Exam 2 Review

This is a set of review problems for the CS 429 F2021 class's second exam.
It covers everything learned in the middle third of the class, including structs, unions, x-86 architecture, and code generation strategies for various code forms.

# Overview

There are two self-explanatory directories contained in this repository.
The `problems` directory contains the practice problems, and the `solutions` directory contains documented solutions for each problem.

Inside the problems directory, there are subdirectories for each problem type, for different topics covered in class.
A file named `example_problem.txt` in the directory will have a corresponding`example_problem-sol.txt` in the solutions directory, with a detailed explanation.
Most problems will also have corresponding C or Assembly code files, which will follow the same naming scheme.

# Testing Your Answers

Obviously, it defeats the purpose of practicing if you immediately look at the solutions, so I've included a way to test them to know if your answer is correct or not, without seeing the actual solution, in case you want to try again.
Inside each problem subdirectory, there's a file named `sol.txt`, where you can write your answers, and a python script named `check_correctness.py`, which you can invoke with `python3 check_correctness.py` in the terminal.


# Generating New Problems (Work in Progress)

In case you solve everything and are looking for more practice, I'm working on implementing generating more problems with a python script.
There is an implemented version in the `problems/structs_unions` directory, if you'd like to take a look.
These problems will not come with detailed solutions (you'll only be told whether your answer is right or wrong), but the questions should follow the same format as the provided problems.
Each problem subdirectory (where applicable) will contain a script `generate.py`, which can be invoked with `python3 generate.py`, and a directory `generated_problem`, which will contain the problem, a `sol.txt` for your answer, a `problem.txt` with the problem description, and any relevant generated code.d
There will also be a `check_correctness.py` inside the directory that is used the same as the main script, for testing your solution to the generated problems.