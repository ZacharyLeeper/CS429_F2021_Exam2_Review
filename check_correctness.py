import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='dir')
parser.add_argument('-g', dest='gen')

def compare_solution(student_answer, solution):
    # Return False for incorrect and True for correct
    correct = []
    for answer, sol in zip(student_answer.readlines(), solution.readlines()):
        if answer.lower() != sol.lower():
            correct.append(False)
    correct.append(True)
    return correct

def print_results(dir, correct_answers):
    print(f'Results for problems in {dir}:')
    for i, correct in enumerate(correct_answers):
        if correct:
            print(f'Problem {i+1} was correct.')
        else:
            print(f'Problem {i+1} was incorrect.')  

if __name__ == "__main__":
    args = parser.parse_args()

    if args.dir:
        if args.gen:
            student_answer = os.path.join('problems', args.dir, 'generated_problem', 'sol.txt')
            solution = os.path.join('problems', args.dir, 'generated_problem', 'answer.txt')
        else:
            student_answer = os.path.join('problems', args.dir, 'sol.txt')
            solution = os.path.join('solutions', args.dir, 'sol.txt')
        with open(student_answer, 'r') as f:
            with open(solution, 'r') as g:
                correct_answers = compare_solution(f,g)
                print_results(args.dir, correct_answers)

    else:
        for root, dirs, files in os.walk(os.path.join('problems')):
            if 'generated_problem' in dirs:
                dirs.remove('generated_problem')
            if 'sol.txt' in files:
                student_answer = os.path.join(root, 'sol.txt')
                solution = os.path.join('solutions', root.split('/')[-1], 'answer.txt')
                with open(student_answer, 'r') as f:
                    with open(solution, 'r') as g:
                        correct_answers = compare_solution(f,g)
                        print_results(args.dir, correct_answers)
                

