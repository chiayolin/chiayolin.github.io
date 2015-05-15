---
layout: post
title:  "Install Packages from AUR"
date:   2014-06-13 11:25:52
categories: linux
---

Arch User Repository (AUR) is a community-driven repository for Arch Linux users. 
You can find packages that haven't been officially supported by Arch Linux on AUR, 
such as Google Chrome, Dropbox, and Libre Office. AUR contains package descriptions 
(PKGBUILDs) that allow you to compile a package from source with makepkg and then 
install it via pacman.

## Getting Started

1\.  Install build essentials: 
  {% highlight bash %} pacman -S --needed base-devel {% endhighlight %}


2\.  Download the tarball of the package you want from [AUR][aur]. 
Then switch your working directory to where your tarball is:
  {% highlight bash %} cd /path/to/directory/ {% endhighlight %}


3\.  Extract the tarball that you downloaded by uing `tar`:
  {% highlight bash %} tar -zxvf FOOBAR.tar.gz {% endhighlight %} 


4\.  `cd` into extracted folder:
  {% highlight bash %} cd /path/to/FOOBAR/ {% endhighlight %}


5\.  Make the package:
  {% highlight bash %}
  makepkg -Acs
  # do not run makepkg as root!
  {% endhighlight %} 


6\.  Finally, install the package with filetype `pkg.tar.xz`
  {% highlight bash %} pacman -U FOOBAR.pkg.tar.xz {% endhighlight %}

That's pretty much it :D

[aur]: https://aur.archlinux.org/
