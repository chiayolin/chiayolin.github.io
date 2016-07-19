# chiayolin.org

[chiayolin.org][1] is the hompage of Chiayo Lin. The site is generated using 
Pelican and published on Github Pages as a user page. You can find the source
code of this project at the `source` branch. The generated source code is
published at the `master` branch.

## Site Generation

To compile the files inside `content/`, run:

```sh
$ make html
```

To start up a local http server:

```sh
$ make serve
```

Alternatively, execute:

```sh
$ sh develop_server.sh
```

## Deploying to Github

Paste the following commands at a terminal prompt to deploy the generated files
insie `output` directory to Github Pages as a user page:

```sh
$ ghp-import output/
$ git checkout master
$ git merge gh-pages
$ git push --all
```

## License

The site is licensed under the MIT License.
