Title:  Installing AUR Packages
Date:   2014-06-13 11:25:52
Modified: 2016-07-18 22:48:30

Arch User Repository (AUR) is a community-driven repository for Arch Linux users. 
You can find packages that haven't been officially supported by Arch Linux on AUR, 
such as Google Chrome, Dropbox, and Libre Office. AUR contains package descriptions 
(PKGBUILDs) that allow you to compile a package from source with makepkg and then 
install it via pacman.

## Getting Started

1\.  Install build essentials: 

	:::sh
	pacman -S --needed base-devel

2\.  Download the tarball of the package you want from [AUR][aur]. 
Then switch your working directory to where your tarball is:

	:::sh
	cd /path/to/directory/

3\.  Extract the tarball that you downloaded by uing `tar`:
  
	:::sh
	tar -zxvf FOOBAR.tar.gz

4\.  `cd` into extracted folder:
  
	:::sh
	cd /path/to/FOOBAR/

5\.  Make the package:
  
	:::sh
	makepkg -Acs
	# do not run makepkg as root!

6\.  Finally, install the package with filetype `pkg.tar.xz`

	:::sh
	pacman -U FOOBAR.pkg.tar.xz

That's pretty much it :D

[aur]: https://aur.archlinux.org/
