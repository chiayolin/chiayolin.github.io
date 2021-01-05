#!/usr/bin/env bash
# source: http://iamemmanouil.com/blog/\
#         static-site-pelican-grunt-travis-github-pages/#deploy

BRANCH="master"
OUTPUT="_output"
NAME="Chiayo Lin"
MAIL="chiayo.lin@gmail.com"
REPO="chiayolin/chiayolin.github.io.git"

echo "testing travis-encrypt"
echo "$VARNAME"

if test "$TRAVIS_PULL_REQUEST" = "false"; then

  if test "$TRAVIS" = "true"; then
    git config --global user.email $MAIL
    git config --global user.name  $NAME
  fi

  # use api token to clone the gh-pages branch
  git clone                                                     \
    --quiet                                                     \
    --branch=$BRANCH https://${GH_TOKEN}@github.com/$REPO built \
      > /dev/null

  # now site is built, cd into that directory and rync target
  cd built
  rsync -rv --exclude=.git  ../$OUTPUT/* .

  echo "remove previous version"
  git rm -rf .
  git clean -f -d
  git commit -m "empty the branch before pushing($TRAVIS_BUILD_NUMBER)"
  git push -fq origin $BRANCH > /dev/null
  cd ..

  echo "deploying to Github Pages"
  # use api token to clone the gh-pages branch again
  git clone                                                     \
    --quiet                                                     \
    --branch=$BRANCH https://${GH_TOKEN}@github.com/$REPO built \
      > /dev/null

  # rync target to the gh-pages branch
  cd built
  rsync -rv --exclude=.git  ../$OUTPUT/* .

  # add, commit, and push files
  git add -f .
  git commit -m "travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
  git push -fq origin $BRANCH > /dev/null

  echo -e "site deployed\n"
fi
