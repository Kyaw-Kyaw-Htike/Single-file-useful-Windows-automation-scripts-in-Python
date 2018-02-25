# Copyright (C) 2018 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.

# Given a full path to a file, find out the hardlinked files associated with the underlying file.

import subprocess
import os

fpath_source = input('Full path to a file to check hardlinks: ')

# remove the double quotes surrounding the fpath_source (if any)
# so that I can add it later properly. (if I don't remove them now, I may accidentally
# add two times which would be wrong.
fpath_source = fpath_source.replace('"', '').replace('\\', '/')

str_cmd = '''fsutil hardlink list "{}"'''.format(fpath_source)
print('Executing the command: ' + str_cmd)
subprocess.call(str_cmd, shell=True)
print('Command executed')