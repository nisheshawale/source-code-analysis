import clang.cindex
import argparse


def find_start_and_end_lines(translation_unit):
    with open("files/outputs/start_and_end_line.txt", "w") as f:
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                start_line = node.location.line
                end_line = node.extent.end.line
                # print(f"Function: {node.spelling}, Start Line: {start_line}, End Line: {end_line}")
                f.write(f"Function: {node.spelling}, Start Line: {start_line}, End Line: {end_line} \n")


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
    find_start_and_end_lines(translation_unit)