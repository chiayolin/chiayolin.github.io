# a simple deployment script for Github Pages
make clean && make html
ghp-import -m "site updates" output
git checkout master
git merge -m "generated content merged" gh-pages
git push --all
git checkout source
