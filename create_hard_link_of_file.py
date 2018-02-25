# Copyright (C) 2018 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.

# Given a full path to a file and a destination directory, create a hardlink of the file and put it in the destination directory.

import subprocess
import os

fpath_source = input('Full path to a file for which to create hardlink: ')
dir_destination = input('Destination directory to place the hardlink: ')

# remove the double quotes surrounding the fpath_source and dir_destination (if any)
# so that I can add it later properly. (if I don't remove them now, I may accidentally
# add two times which would be wrong.
fpath_source = fpath_source.replace('"', '').replace('\\', '/')
dir_destination = dir_destination.replace('"', '').replace('\\', '/')

# if the last character of the given directory is "/", remove it
if dir_destination[-1] == '/':
    dir_destination = dir_destination[:-1]

_, fname_source = os.path.split(fpath_source)
fname_source_no_ext, ext_fname_source = os.path.splitext(fname_source)

# destination hard link file will have the same name as the source file (but with "_hardlink" added)
# which I'm creating the hard link for
fpath_destination = dir_destination + '/' + fname_source_no_ext + '_hardlink' + ext_fname_source

str_cmd = '''mklink /H "{}" "{}"'''.format(fpath_destination, fpath_source)
print('Executing the command: ' + str_cmd)
subprocess.call(str_cmd, shell=True)
print('Command executed')
