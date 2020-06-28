#Problem 2 : File Recursion
import os

def find_files(suffix, path):
    list_paths = []
    
    for file in os.listdir(path):
        if os.path.isdir(file):
            path = os.path.join(path, file)
            find_files(suffix, path)
       
        if file.lower().endswith(suffix):
            path_file = os.path.dirname(file)
            list_paths.append(path_file)
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    return list_paths
  
 
#Test 
path = os.getcwd() + '/testdir'
# Test Case 1 
find_files('.c', path)
# [./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir5/a.c, ./testdir/subdir1/a.c, ./testdir t1.c]

# Test Case 2
find_files('.h', path)
# [./testdir/subdir3/subsubdir1/b.h, ./testdir/subdir5/a.h, ./testdir/subdir1 a.h, ./testdir t1.h]

# Test Case 3
find_files('.z', path)
# []
