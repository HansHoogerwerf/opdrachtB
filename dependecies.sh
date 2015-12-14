echo "installing all dependecies!"

sudo apt-get install python-psycopg2 -y
sudo pip install --quiet sqlalchemy
sudo pip install --quiet nosexcover
sudo pip install --quiet nose
sudo pip install --quiet pylint

echo "installed dependecies"

