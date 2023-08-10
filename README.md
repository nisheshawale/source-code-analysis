# Source Code Analysis

This code can analyze the C/C++ functions in Python. This repo uses the [clang](https://pypi.org/project/clang/16.0.1.1/#description) library in Python to perform the following tasks.

1. For each function, identify its function name, parameter types, and returned value type.
2. For each function, find what other functions it has called.
3. For each function, output its start and end line.
4. For any two functions, output their differences (similar to ‘diff’).

The input files are given in the *files/inputs* directory.

## Install the dependencies

1. Use Python version 3.10. If you have 3.10 installed, proceed to step 2. Otherwise, run the following commands.
```
sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10
python3.10 --version
```

2. Install Clang
```
sudo apt install clang
``` 

3. Install llvm and libclang
```
sudo apt-get install llvm libclang-dev
```

4. Create a new virtual environment and activate it.

```
python3.10 -m venv source-code-analysis-env
source source-code-analysis-env/bin/activate
```

5. Install the requirements
```
pip install -r requirements.txt
```

## Running the code

After the installation process is complete, you have to find where the libclang.so file is using the following command.
```
dpkg-query -S libclang.so
```
Suppose it output the path as your_libclang_directory_path/libclang.so, then you use the path up to the libclang directory in the following commands.

### For task 1
```
python3.10 name_parameters_return_value.py --file files/foo.c --library_path your_libclang_directory_path
```

### For task 2
```
python3.10 other_functions_called.py --file files/foo.c --library_path your_libclang_directory_path
```

### For task 3
```
python3.10 start_and_end_line.py --file files/foo.c --library_path your_libclang_directory_path
```

### For task 4
```
python3.10 differences.py --file1 files/inputs/f1.c --file2 files/inputs/f2.c
```

The outputs of each tasks are stored in the *files/outputs* directory.


