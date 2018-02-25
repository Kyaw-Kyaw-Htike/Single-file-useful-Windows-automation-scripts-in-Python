# print the ennvironment variable 'path' in a nice format.

import os

path_strings = os.environ['PATH'].split(os.pathsep);
for i in range(len(path_strings)):
	print(i+1, path_strings[i])