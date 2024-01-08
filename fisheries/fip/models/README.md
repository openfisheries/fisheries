```bash
pip install sqlalchemy geoalchemy2 psycopg2-binary
sudo apt install sqlacodegen
sqlacodegen postgresql+psycopg2://fip:admin@localhost:5432/fip --outfile models/__init__.py
```
