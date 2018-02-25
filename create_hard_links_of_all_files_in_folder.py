# Copyright (C) 2018 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.

# Given a source directory and a destination directory, create a hardlinks of all the files
# in the given directory and place them in the destination directory

import subprocess
import os

dir_source = input('Source directory to make hardlinks from: ')
dir_destination = input('Destination directory to place the created hardlinks: ')

# remove the double quotes (if any) surrounding the dir_source and dir_destination
# so that I can add it later properly. (if I don't remove them now, I may accidentally
# add two times which would be wrong.
dir_source = dir_source.replace('"', '').replace('\\', '/')
dir_destination = dir_destination.replace('"', '').replace('\\', '/')

# if the last character of the given directory is "/", remove it
if dir_source[-1] == '/':
    dir_source = dir_source[:-1]
if dir_destination[-1] == '/':
    dir_destination = dir_destination[:-1]

# get list of all file names in the given directory
fnames_source = [f for f in os.listdir(dir_source) if os.path.isfile(os.path.join(dir_source, f))]

for fname_source in fnames_source:
    fpath_source = dir_source + '/' + fname_source
    fpath_destination = dir_destination + '/' + fname_source

    str_cmd = '''mklink /H "{}" "{}"'''.format(fpath_destination, fpath_source)
    print('Executing the command: ' + str_cmd)
    subprocess.call(str_cmd, shell=True)
    print('Command executed')


#
# _, fname_source = os.path.split(fpath_source)
# fname_source_no_ext, ext_fname_source = os.path.splitext(fname_source)
#
# # destination hard link file will have the same name as the source file (but with "_hardlink" added)
# # which I'm creating the hard link for
# fpath_destination = dir_destination + '/' + fname_source_no_ext + '_hardlink' + ext_fname_source
#
# str_cmd = '''mklink /H "{}" "{}"'''.format(fpath_destination, fpath_source)
# print('Executing the command: ' + str_cmd)
# subprocess.call(str_cmd, shell=True)
# print('Command executed')
