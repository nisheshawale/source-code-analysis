import clang.cindex
import argparse


def find_name_arguments_return_type(translation_unit):
    with open("files/outputs/name_parameters_return_value.txt", "w") as f:
        for node in translation_unit.cursor.walk_preorder():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                # print(f"Function Name :- {node.spelling}")
                f.write(f"Function Name :- {node.spelling} \n")
                try:
                    args = node.type.argument_types()
                    for arg in args:
                        # print(f"Function Arguments :- {arg.spelling}")
                        f.write(f"Function Arguments :- {arg.spelling} \n")
                except:
                    # print(f"Function Arguments :- None")
                    f.write(f"Function Arguments :- None \n")

                # print(f"Return type :- {node.result_type.spelling}")
                f.write(f"Return type :- {node.result_type.spelling} \n")


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
    find_name_arguments_return_type(translation_unit)