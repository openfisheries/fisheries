```bash
pip install sqlalchemy geoalchemy2 psycopg2-binary
# sudo apt install sqlacodegen  # apt install gives 1.1.6, we need 2.1.0+
# https://stackoverflow.com/a/36699285/1624894
# sudo apt-get remove sqlacodegen
pip install --user sqlacodegen  # ~/.local/bin/sqlacodegen --version
~/.local/bin/sqlacodegen postgresql+psycopg2://fip:admin@localhost:5432/fip --outfile ~/fisheries/fisheries/fip/models/__init__.py

```
