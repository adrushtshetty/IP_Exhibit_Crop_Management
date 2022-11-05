# with open("trial.html", "r") as in_file:
#     buf = in_file.readlines()
# crop=input("Display Crop Name")
# with open("trial.html", "w") as out_file:
#     for line in buf:
#         if line == "; <!--name of crop-->\n":
#             # line = line + "Include below\n"
#             line=crop
#             print("Changed")
#         out_file.write(line)

# def find_append_to_file(filename, find, insert):
#     """Find and append text in a file."""
#     with open(filename, 'r+') as file:
#         lines = file.read()
#
#         index = repr(lines).find(find) - 1
#         if index < 0:
#             raise ValueError("The text was not found in the file!")
#
#         len_found = len(find) - 1
#         old_lines = lines[index + len_found:]
#
#         file.seek(index)
#         file.write(insert)
#         file.write(old_lines)
#
# find_append_to_file("trial.html","<!--name of crop-->","360 Ugo boga")

import fileinput
filename="trial.html"
for line in fileinput.FileInput(filename,inplace=1):
    if "<!--here-->" in line:
        line=line.rstrip()
        line=line.replace(line,"Hello World")
    print (line)

