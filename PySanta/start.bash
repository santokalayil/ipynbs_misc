# open git bash termial
alias subl="/c/Program\ Files/Sublime\ Text\ 3/sublime_text.exe"
subl .

python -m venv env # creating virtual environment with folder name env that holds virtual environment

mkdir project

source env/Scripts/activate

# pip install required libraries and export the list to requirements.txt
python -m pip install --upgrade pip

pip3 freeze > requirements.txt # to export

pip install -r requirements.txt # to instal from requirements.txt