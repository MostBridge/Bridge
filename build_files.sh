pip install -r requirements/requirements.txt
python3.11 manage.py collectstatic --noinput

python3.11 manage.py migrate 

echo "Collect Static..."
python3.11 manage.py collectstatic 
