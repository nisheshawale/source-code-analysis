import clang.cindex
import argparse


def find_function_calls(cursor):
    function_calls = []

    for node in cursor.walk_preorder():
        if node.kind == clang.cindex.CursorKind.CALL_EXPR:
            function_calls.append(node.displayname)

    return function_calls


def other_functions_called(translation_unit):
    with open("files/outputs/other_functions_called.txt", "w") as f:
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                function_calls = find_function_calls(node)
                # print("Function Calls in 'main':", function_calls)
                f.write(f"Function Calls in {node.spelling}: {function_calls} \n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Source code analysis')
    parser.add_argument('-f', '--file', help='Path to input C file', required=True)
    parser.add_argument('--library_path', help='Path to libclang.so file', required=True)

    args = parser.parse_args()

    c_file_path = args.file
    library_path = args.library_path

    # clang.cindex.Config.set_library_path("/home/nishesh/Desktop/source-code-analysis/source-code-env/lib64/python3.10/site-packages/clang")
    clang.cindex.Config.set_library_path(library_path)

    index = clang.cindex.Index.create()
    translation_unit = index.parse(c_file_path)
    other_functions_called(translation_unit)