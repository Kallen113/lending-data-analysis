# import zipfile

import shutil

import os


def main():

    # unzip the lending data file
    # specify the zipped file name
    zipped_file = 'approved_data_2016_2018.zip'

    # use os.getcwd() as argument for path--by specifying current directory--to extract the unzipped file, given zipped file name
    shutil.unpack_archive(zipped_file, os.getcwd())


if __name__ == '__main__':
    main()