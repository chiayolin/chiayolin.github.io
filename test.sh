# test.sh - render and run the site locally
#
# $ sh test.sh

# install requirements
pip3 install -r requirements.txt

# render the site
python3 render.py

# serve rendered web pages
cd _output
python3 -m http.server && cd ..
