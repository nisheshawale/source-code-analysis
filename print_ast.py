import clang.cindex
import argparse


def print_ast(cursor):
    with open("files/outputs/ast.txt", "w") as f:
        def traverse_cursor(cursor, depth=0):
            # print("    " * depth, cursor.kind, cursor.spelling)
            f.write(f"{'    ' * depth} {cursor.kind} {cursor.spelling} \n")
            for child in cursor.get_children():
                traverse_cursor(child, depth + 1)

        traverse_cursor(cursor)


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
    print_ast(translation_unit.cursor)