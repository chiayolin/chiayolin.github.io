---
title    : Installing AUR Packages
date     : 2014-06-13
modified : 2016-07-18
location : Saigon, Vietnam
---

Arch User Repository (AUR) is a community-driven repository for Arch Linux users.
You can find packages that haven't been officially supported by Arch Linux on AUR,
such as Google Chrome, Dropbox, and Libre Office. AUR contains package descriptions
(PKGBUILDs) that allow you to compile a package from source with makepkg and then
install it via pacman.

## Getting Started

First install build essentials:

```sh
$ pacman -S --needed base-devel
```

After the built essentials are installed, download the tarball of the package that
you want from [AUR][aur]. And switch your current working directory to where the
tarball is at:

```sh
$ cd /path/to/directory/
```

Simply extract the tarball using the `tar` command:

```sh
$ tar -zxvf FOOBAR.tar.gz
```

`cd` into the extracted folder:

```sh
$ cd /path/to/FOOBAR/
```

Make the package using `makepkg`:


```sh
$ makepkg -Acs
# do not run makepkg as root!
```

Finally, install the package with the extension `.pkg.tar.xz`

```sh
$ pacman -U FOOBAR.pkg.tar.xz
```

And then you are ready to go :D

[aur]: https://aur.archlinux.org/
