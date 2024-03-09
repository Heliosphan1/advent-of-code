import json
import os 
import requests
import time

from bs4 import BeautifulSoup
from collections import defaultdict

first_year = 2015
last_year = 2023
first_day = 2
last_day = 25
USER_SESSION_ID = '53616c7465645f5f904a68e60707f224da60a88fa6bbcbffe9cfe3666726bd43c54434544cf5ea82e5ec5070d435196f4c860c51a3c0851fccea5e24ccaac9ae'
OUTPUT_FOLDER = 'D:\code_projects\Advent of Code'
OVERWRITE = False
MAX_RETRIES = 3
WAIT_TIME = 1

with open('programming_language_extensions.json', 'r') as json_file:
    data = json.load(json_file)
    extensions = {lang['name']: lang['extensions'] for lang in data}


def get_puzzle_description(year, day):
    retry_count = 0
    url = f'https://adventofcode.com/{year}/day/{day}'
    while retry_count <= MAX_RETRIES:
        try:
            r = requests.get(url)
            if r.ok:
                soup = BeautifulSoup(r.content, 'html.parser')
                article = soup.find('article')
                return(str(article))
            r.raise_for_status()
        except requests.RequestException:
            retry_count += 1
            if retry_count > MAX_RETRIES:
                print(f'Could not download description for {year}-{day}, number of retries exceeded')
                return ''
            print(f'Retrying connection {retry_count}/{MAX_RETRIES}')
            time.sleep(WAIT_TIME * retry_count)
        except Exception as e:
            print(f'Unknown error - {e}')
            raise
            
def get_inputs(year, day):
    retry_count = 0
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    while retry_count <= MAX_RETRIES:
        try:
            r = requests.get(url, cookies={'session': USER_SESSION_ID}, timeout=30)
            if r.ok:
                return r.text
            r.raise_for_status()
        except requests.RequestException:
            retry_count += 1
            if retry_count > MAX_RETRIES:
                print(f'Could not download input for {year}-{day}, number of retries exceeded')
                return ''
            print(f'Retrying connection {retry_count}/{MAX_RETRIES}')
            time.sleep(WAIT_TIME * retry_count)
        except Exception as e:
            print(f'Unknown error - {e}')
            raise
        

def create_structure(extensions=['.py']):

    for y in range(max(first_year, 2015), last_year + 1):
        year_folder = os.path.join(OUTPUT_FOLDER, str(y))
        if not os.path.exists(year_folder):
            os.mkdir(year_folder)
            
        for d in range(first_day, min(last_day, 25) + 1):
            str_d = f'0{d}' if d < 10 else str(d)
            day_folder = os.path.join(year_folder, str_d)
            if not os.path.exists(day_folder):
                os.mkdir(day_folder)
                
            for ext in extensions:
                filename = os.path.join(day_folder, f'aoc_{y}_{str_d}{ext}')
                if not os.path.exists(filename):
                    with open(filename, 'w+') as code_file:
                        header = f'# Advent of Code - {y} - day {d}\n\n' + \
                                'with open("input.txt") as input_file:\n' + \
                                '    input = input_file.read()'
                        code_file.write(header)
            
            print(f'downloading inputs for {y}-{d}')
            input_data = get_inputs(y, d)
            with open(os.path.join(day_folder,'input.txt'), 'w') as f:
                f.write(input_data)
                
            print(f'downloading description for {y}-{d}')
            puzzle_desc = get_puzzle_description(y, d)
            with open(os.path.join(day_folder, 'description.html'), 'w') as f:
                f.write(puzzle_desc)
            
if __name__ == "__main__":
    create_structure()
