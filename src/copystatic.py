from os import listdir, mkdir
from os.path import exists, isfile, join
from shutil import copy, rmtree

def copy_static(src, dst):
    print(f"src: {src}\ndst: {dst}")
    if exists(dst):
        rmtree(dst)
        mkdir(dst)
    else:
        mkdir(dst)

    def copy_src(src, dst):
        for entry in listdir(src):
            src_entry = join(src, entry)
            dst_entry = join(dst, entry)

            if isfile(src_entry):
                copy(src_entry, dst)
            else:
                mkdir(dst_entry)
                copy_src(src_entry, dst_entry)

    copy_src(src, dst)