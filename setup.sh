virtualenv -p python3.6 _env
source _env/bin/activate
pip install -r requirements.txt
export FLASK_APP=anagrams.py
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
echo "flask run --host=0.0.0.0"