import library as lib
import os
with open(os.path.abspath('Files/input.txt'), "r") as f:
    content = f.readlines()
    file = lib.get_file(content)
    sections = lib.get_section(file)
    d = lib.dictionary(sections, file)
    if len(d):
        lib.test_sigma(d)
        lib.test_start_final(d)
        lib.test_delta(d)
