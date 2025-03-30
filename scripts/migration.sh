set -e
set -x

# a lancer sur python-anywhere.com

echo "=== lancement des migrations ==="
python manage.py migrate

echo "=== collecte des fichiers statiques ==="
python manage.py collectstatic --noinput

echo "=== fin des migrations ==="
