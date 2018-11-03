#!/usr/bin/env bash
# source: http://iamemmanouil.com/blog/\
#         static-site-pelican-grunt-travis-github-pages/#deploy
BRANCH=master
TARGET_REPO=chiayolin/chiayolin.github.io.git
OUTPUT_FOLDER=_output

echo -e "testing travis-encrypt"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then

    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "chiayo.lin@gmail.com"
        git config --global user.name "Chiayo Lin"
    fi

    # Using token clone gh-pages branch
    git clone --quiet --branch=$BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null

    # Go into directory and copy data we're interested in to that directory
    cd built_website
    rsync -rv --exclude=.git  ../$OUTPUT_FOLDER/* .

    echo -e "remove previous version of website\n"
    git rm -rf .
    git clean -f -d
    git commit -m "empty the branch before pushing($TRAVIS_BUILD_NUMBER)"
    git push -fq origin $BRANCH > /dev/null
    cd ..

    echo -e "starting deployment on Github Pages\n"
    # Using token clone gh-pages branch
    git clone --quiet --branch=$BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null

    # Go into directory and copy data we're interested in to that directory
    cd built_website
    rsync -rv --exclude=.git  ../$OUTPUT_FOLDER/* .

    # Add, commit and push files
    git add -f .
    git commit -m "travis build $TRAVIS_BUILD_NUMBER pushed to Github Pages"
    git push -fq origin $BRANCH > /dev/null

    echo -e "deploy completed\n"
fi
