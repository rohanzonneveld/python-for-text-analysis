from utils import get_paths, get_basic_stats
import os
input_folder = 'Data/books'
paths = get_paths(input_folder)
print(paths)

book2stats = {}
for path in paths:
    stats = get_basic_stats(os.path.join(input_folder, path))
    basename = os.path.basename(path).split('.')[0]
    # print(f'{basename}: {stats}')
    book2stats[basename] = stats
    with open(f'Assignments/ASSIGNMENT_3_ROHAN_ZONNEVELD/top_30_{path}', 'w') as f:
        for token in stats['top_30_tokens']:
            f.write(str(token[0]) + '\n')

stats2book_with_highest_value = {}
for key in book2stats[basename].keys():
    stats2book_with_highest_value[key] = max(book2stats, key=lambda x: book2stats[x][key])

print(stats2book_with_highest_value)

