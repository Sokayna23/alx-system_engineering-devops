#!/bin/bash
0. Where am I?
           pwd : prints the absolute path name of the current working directory.
1. What’s in there?
	ls : displays the contents list of your current directory.
2. There is no place like home
	cd ~ : changes the working directory to the user’s home directory.
3. The long format
	ls -l : displays current directory contents in a long format
4. Hidden files
	ls -la : Displays current directory contents, including hidden files (starting with .). Uses  the long format.
5. I love numbers
	ls -la -n : “ls” displays current directory contents, the  “l” option  displays it with long format,
and the “n” option displays user and group IDs numerically and the  “a” option displays hidden files (starting with .).
6. Welcome
	mkdir /tmp/my_first_directory : creates a directory named my_first_directory in the /tmp/ directory.
7. Betty in my first directory
	 mv /tmp/betty /tmp/my_first_directory : moves the file betty from /tmp/ to /tmp/my_first_directory.
8. Bye bye Betty
	rm /tmp/my_first_directory/betty : deletes the file betty that’s in /tmp/my_first_directory.
9. Bye bye My first directory
	rmdir /tmp/my_first_directory : deletes the directory my_first_directory that is in the /tmp directory.
10. Back to the future
	cd - : changes the working directory to the previous one.
11. Lists
	ls -la .. /boot :  lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12. File type
	file /tmp/iamafile : prints the type of the file named iamafile. The file iamafile will be in the /tmp directory.
13. We are symbols, and inhabit symbols
	ln -s /bin/ls __ls__ : creates a symbolic link to /bin/ls, named __ls__
14. Copy HTML files
	cp ./*.html ../ : copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
15. Let’s move
	mv [[:upper:]]* /tmp/u :  moves all files beginning with an uppercase letter to the directory /tmp/u.
16. Clean Emacs
	rm ./*~ : deletes all files in the current working directory that end with the character ~.
17. Tree
	mkdir -p welcome/to/school :   creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory using only two spaces in the script.
18. Life is a series of commas, not periods
 
