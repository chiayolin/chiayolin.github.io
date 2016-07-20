# chiayolin.org [![Build Status](https://travis-ci.org/chiayolin/chiayolin.github.io.svg?branch=source)](https://travis-ci.org/chiayolin/chiayolin.github.io)

[chiayolin.org][1] is the hompage of Chiayo Lin. The site is generated using 
Pelican and published on Github Pages as a user page. You can find the source
code of this project at the `source` branch. The generated source code is
published at the `master` branch.

## Site Generation

To compile the files inside `content/`, run:

```sh
$ make html
```

To start up a local HTTP server:

```sh
$ make serve
```

Alternatively, execute:

```sh
$ sh develop_server.sh
```

## Deploying to Github

Paste the following commands at a terminal prompt to deploy: 

```sh
$ ghp-import output/  # import the generated filse in `output/` to `gh-pages`
$ git checkout master # switch to `master` 
$ git merge gh-pages  # merge the imported files
$ git push --all      # push it to Gihutb
```

## License

The site is licensed under the MIT License.

[1]: http://chiayolin.org/
