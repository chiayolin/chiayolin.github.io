# test.sh - render and run the site locally
#
# $ sh test.sh

python3 render.py
cd _output
python3 -m http.server && cd ..
