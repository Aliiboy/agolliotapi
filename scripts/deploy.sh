set -e
set -x

# a lancer sur python-anywhere.com

git clean -f
git restore .
git pull 

REQUIREMENTS_FILE="/home/agolliot/agolliotapi/requirements.txt"

echo "=== Désinstallation de tous les packages Python existants ==="
pip freeze | xargs pip uninstall -y

echo "=== Réinstallation des packages depuis $REQUIREMENTS_FILE ==="
pip install -r "$REQUIREMENTS_FILE"

echo "=== Mise à jour des dépendances terminée ==="
