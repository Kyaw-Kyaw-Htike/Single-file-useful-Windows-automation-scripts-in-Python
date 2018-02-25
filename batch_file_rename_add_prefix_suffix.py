# python script for batch file renaming by adding a prefix and a suffix

import os

# directory where the images are
dir_files = 'C:/Users/SomeUser/SomeFolder/SomeOtherFolder'
# prefix in front of the file name to insert
str_prefix = 'proj_'
# suffix at the end of the file name to insert
str_suffix = '_image'

filenames = os.listdir(dir_files)
for filename in filenames:
    filename_no_ext, file_extension = os.path.splitext(filename)
    os.rename(os.path.join(dir_files, filename), os.path.join(dir_files, str_prefix + filename_no_ext + str_suffix + file_extension))



