import concurrent.futures
import time

import requests

def get_pokemon_name(id):
    with requests.Session() as s:
        response = s.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    s.close()
    result = response.json()['name']
    print(result)


if __name__ == '__main__':
    start = time.time()
    pokemon_id = range(1,10)
    [get_pokemon_name(x) for x in pokemon_id]
    print('processing time: %.2f seconds' % (time.time() - start))

    # multi processingpool
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(get_pokemon_name, pokemon_id)
    print('processing time: %.2f seconds' % (time.time() - start))

    # multi threadpool
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_pokemon_name, pokemon_id)
    print('processing time: %.2f seconds' % (time.time() - start))