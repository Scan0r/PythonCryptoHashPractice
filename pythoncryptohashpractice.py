#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################
# pythoncryptohashpractice -- Reads a file of words per line, and generates two files with
# the words encrypted by md5 and sha1 in each one
#
# Copyright (c) 2021, Scan0r
#
# This program is free software: you can redistribute it and/or modifyç
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# @Author       Scan0r
# @Date         22/11/2021
# @Version      0.1
######################################################################

# Global Imports
from Crypto.Hash import SHA1, MD5


# Global definitions
default_words_file = "words.txt"
sha1_words_file = "sha1_words.txt"
md5_words_file = "md5_words.txt"


def sha1(text: str) -> str:
    ''' Generates the SHA1 hash of a given text '''

    # Creates a new SHA1 instance
    sha1 = SHA1.new()
    # Sets the text as the payload to hash
    sha1.update(text.encode())
    # Generates the hash of the text in hexadecimal format
    return "0x" + sha1.hexdigest()


def md5(text: str) -> str:
    ''' Generates the MD5 hash of a given text '''

    # Creates a new MD5 instance
    md5 = MD5.new()
    # Sets the text as the payload to hash
    md5.update(text.encode())
    # Generates the hash of the text in hexadecimal format
    return "0x" + md5.hexdigest()


def main():
    ''' Reads the words file and for each word, encrypts it using md5 and sha1 and stores it in two files '''

    # Opens the words file, and creates the hashes files
    with open(default_words_file, 'r') as dwf, open(sha1_words_file, 'w') as swf, open(md5_words_file, 'w') as mwf:
        # Reads all the lines of words
        words = dwf.readlines()
        # Prints the number of lines read
        print(f'[+] Read {len(words)} lines from file "{default_words_file}"\n')
        # Iterates over every word
        for word in words:
            # Deletes the unnecessary spaces and line breaks on the line
            word = word.strip()
            # Generates the hashes of the word
            sha1_word = sha1(word)
            md5_word = md5(word)
            # Stores the hashes in every hash file
            swf.write(sha1_word + "\n")
            mwf.write(md5_word + "\n")
            # Prints a informative message with the opertions done
            print(f'Written hash SHA1("{word}") == "{sha1_word}" to file "{sha1_words_file}"')
            print(f'Written hash MD5("{word}") == "{md5_word}" to file "{md5_words_file}"')
            print()


# Calls the main function of the program
if __name__ == '__main__':
    main()
