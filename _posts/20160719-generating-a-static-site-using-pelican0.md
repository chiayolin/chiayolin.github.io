---
title    : Generating a Static Site with Pelican
date     : 2016-07-19
modified : 2017-05-01
location : Centreville, Virginia
---

I used [Jekyll][1] as a static site generator to generate HTML files from
[Markdown][2] for this site and it worked just fine. However, Jekyll was perhaps
too powerful for what I really needed. Because what I wanted was just a simple static
site generator that parses my templates and Markdown files and outputs HTMLs, without
spending time configuring different versions of Ruby Gems just to get my site up
and running. So I recently decided to give [Pelican][3] a try. Pelican is a
static generator like Jekyll, but it is written in [Python][4] and uses
[Jinja][5] as its templating language/engine. This post is created as a note to
myself about generating a static site with Pelican.

[1]: https://jekyllrb.com/
[2]: https://en.wikipedia.org/wiki/Markdown
[3]: http://blog.getpelican.com/
[4]: https://www.python.org/
[5]: http://jinja.pocoo.org/


## Installation

First thing we want to do is install Pelican and Markdown via `pip` and update
your Python if it is needed:

```sh
$ pip install pelican markdown
```

## Create a Project

After Pelican is installed on your machine, you may now begin creating a directory
for your Pelican site:

```sh
$ mkdir awsome_project
$ cd awsome_project
```

After your project directory is created, run the `pelican-quickstart` command to
proceed the process of creating a Pelican project:

```sh
$ pelican-quickstart
```

By running `pelican-quickstart`, the script will ask you some questions regarding
the configuation of your site (this post will assume that you leave the choices
as default). Answer these questions truthfully XD

You might also want to initialize the project directory as a Git repository in
order to keep track of your code and later push them to [Github Pages][6].
(I will write another post on deploying a Pelican site to Github Pages).

```sh
$ git init
$ git remote add origin git@github.com:username/awsome_project.git
```

[6]: https://pages.github.com/

## Site Generation
I don't remember any one of the Pelican commands... But hey, if you decided to
generate a [Makefile][10] in the previous section when running the
`pelican-quickstart` command then all you need to do now is run:

```sh
$ make html
```
[10]: https://en.wikipedia.org/wiki/Makefile

Yes, that's it. A Pelican site is generated under the `output/` directory.

## Run a HTTP Server Locally

"Running a HTTP Server Locally" is basically just a fancy way to say "preview your
site before publishing it." In order to do that, simply type the command below at
a terminal prompt inside your project's root directory (where your Makefile is):

```sh
$ make serve
```

Alternatively, run `develop_server.sh`:

```sh
$ sh develop_server.sh
```

This will automatically regenerate the site when a change is made.

Finally, you can navigate to [http://localhost:8000/][7] in your browser
to access/preview the generated site.

[7]: http://localhost:8000/

## Writting Content

Every Markdown file (or whatever tool you prefer) and other files for the site are
placed under the `content/` directory. For more information about writting the
content, please head to the [offical documentation][8].

[8]: http://docs.getpelican.com/en/3.6.3/content.html
