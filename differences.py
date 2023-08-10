import difflib
import argparse

def compare_functions(function1, function2):
    # Parse the source code of both functions
    parsed_function1 = function1.splitlines()
    parsed_function2 = function2.splitlines()

    # Calculate the difference between the two parsed functions
    differ = difflib.Differ()
    diff = list(differ.compare(parsed_function1, parsed_function2))

    # Output the differences
    with open("files/outputs/differences.txt", "w") as f:
        for line in diff:
            # print(line)
            f.write(f"{line} \n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Source code analysis')
    parser.add_argument('-f1', '--file1', help='Path to first input C file', required=True)
    parser.add_argument('-f2', '--file2', help='Path to second input C file', required=True)
    # parser.add_argument('--library_path', help='Path to libclang.so file', required=True)

    args = parser.parse_args()

    c_file_path_1 = args.file1
    c_file_path_2 = args.file2
    # library_path = args.library_path

    with open(c_file_path_1, 'r') as f1:
        function1 = f1.read()

    with open(c_file_path_2, 'r') as f2:
        function2 = f2.read()
    
    compare_functions(function1, function2)