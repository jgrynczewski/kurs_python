# Moduły

# Pobierz zawartość strony www.wp.pl
import requests

res = requests.get('https://www.wp.pl')

print(res.text)
