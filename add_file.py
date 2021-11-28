import os
from typing import final

list_file = []

list_item_file = os.listdir('vault')

for item in list_item_file:

    with open(f'vault/{item}', encoding='utf-8') as file:

        content_lines = file.readlines()
        content = [item + '\n'] + [str(len(content_lines)) + '\n'] + content_lines + ['\n']
        list_file.append(content)

text = ' '.join(sum((sorted(list_file, key=len)), []))

with open('final_file.txt', 'w', encoding='utf-8') as add_file:
    add_file.write(text)
file.close()